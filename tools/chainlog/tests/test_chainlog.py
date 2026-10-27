import json
import os
import sys
import tempfile
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
import chainlog  # noqa: E402


def write(path, lines):
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write("\n".join(lines) + "\n")


class ChainlogTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.log = os.path.join(self.tmp.name, "log.ndjson")
        self.lines = [json.dumps({"i": i, "t": "message %d 中文" % i}, ensure_ascii=False) for i in range(1, 8)]
        write(self.log, self.lines)
        self.out = os.path.join(self.tmp.name, "b")
        chainlog.build(self.log, self.out, "1-3")

    def tearDown(self):
        self.tmp.cleanup()

    def test_clean_bundle_verifies_with_and_without_source(self):
        self.assertEqual(chainlog.verify(self.out), [])
        self.assertEqual(chainlog.verify(self.out, self.log), [])

    def test_crlf_input_gives_the_same_root(self):
        crlf = os.path.join(self.tmp.name, "crlf.ndjson")
        with open(crlf, "w", encoding="utf-8", newline="") as fh:
            fh.write("\r\n".join(self.lines) + "\r\n")
        other = os.path.join(self.tmp.name, "b2")
        m1 = chainlog.build(self.log, self.out)
        m2 = chainlog.build(crlf, other)
        self.assertEqual(m1["root"], m2["root"])

    def test_one_edited_line_in_the_source_is_found(self):
        edited = list(self.lines)
        edited[4] = edited[4].replace("message 5", "message 5!")
        bad = os.path.join(self.tmp.name, "bad.ndjson")
        write(bad, edited)
        problems = chainlog.verify(self.out, bad)
        self.assertTrue(any("source line 5" in p for p in problems))

    def test_commit_digest_changes_when_the_log_changes(self):
        d1 = chainlog.commit_digest(self.out)
        write(self.log, self.lines[:-1])
        chainlog.build(self.log, self.out)
        self.assertNotEqual(d1, chainlog.commit_digest(self.out))

    def test_empty_log(self):
        empty = os.path.join(self.tmp.name, "empty.ndjson")
        open(empty, "w").close()
        out = os.path.join(self.tmp.name, "e")
        chainlog.build(empty, out)
        self.assertEqual(chainlog.verify(out, empty), [])

    def test_selftest(self):
        self.assertTrue(chainlog.selftest())


if __name__ == "__main__":
    unittest.main()
