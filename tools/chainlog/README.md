# chainlog

A small tool for making a chat log tamper-evident, so that a reader can check later that nothing was changed after you fixed it. It needs only Python 3 and the standard library.

It exists because the AI Philosophy Competition asks entrants to retain chat logs and may ask for them, and because public discussion of the competition points out that a log can be edited. A hash chain cannot show who had an idea. It can show that the log you release is the log you committed to earlier.

## The scheme

```
leaf_i  = SHA-256(raw line i, UTF-8, no line terminator)
chain_0 = SHA-256("CHAINLOG-v1")
chain_i = SHA-256(chain_{i-1} || leaf_i)        # both as 32 raw bytes
root    = chain_n
```

Reordering, deleting, inserting or editing any line changes every later chain value and the root.

A bundle is a folder with `manifest.json` (format, record count, root), `leaves.csv` (one row of hashes per record) and optionally `disclosed.jsonl` (the records you choose to publish in full). Records you do not publish stay checkable as hashes, so you can release part of a log and still commit to all of it.

## Use

```
python chainlog.py build  log.ndjson bundle/ --disclose 1-20,45
python chainlog.py verify bundle/                       # bundle is self-consistent
python chainlog.py verify bundle/ --source log.ndjson   # and matches the original file, line by line
python chainlog.py commit bundle/                       # digest of manifest.json: post this as your commitment
python chainlog.py selftest
```

`examples/` holds a synthetic 12-record log and the bundle built from it. `python -m unittest discover tests` runs the tests.

## What it does not do

- It does not prove authorship, or that the log is complete. A conversation held outside the logged channel is invisible to it.
- It trusts the order of lines as you give it. If your platform's log can be rewritten before you hash it, the chain commits to the rewritten log.
- A date comes from wherever you publish the commitment. Posting the digest somewhere with its own timestamp (a forum comment, a signed commit, an OpenTimestamps proof) is what makes the date independent of you.

Licence: MIT (see the repository's LICENSE).
