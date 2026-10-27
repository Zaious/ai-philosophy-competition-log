# Commitments

These are the SHA-256 digests of the essays and methodology reports submitted to the AI Philosophy Competition 2026. File names are neutral on purpose. The files themselves are not published here until results are announced.

| File | SHA-256 |
|---|---|
| submission_1/submission1_essay.pdf | `b8443eec4dd0ebe15fa11f283b1ef6760891731e16c85575e66167e62fc4954d` |
| submission_1/submission1_methodology_report.pdf | `91212f7ac47f5f9e3179c86595dbfb191124957ac0d9cde2e9d8563195d8166c` |
| submission_2/submission2_essay.pdf | `6a81ed654d8f61a470e70ff82da047e440b02599f9a465701656e658d814dc49` |
| submission_2/submission2_methodology_report.pdf | `cdf43108fc9f90f66fb08aa1edf9d52b28f32e943fbe56889ca3f8035e1b3cc8` |
| submission_3/submission3_essay.pdf | `026e9cd1710ba952a181c69d3b143685c85aebb5e55781ab974ebd05bee4de47` |
| submission_3/submission3_methodology_report.pdf | `b44c052416d5f9229db92d8080f9c0739229e02ab64803bc65653d75f41a3257` |

The same list is in [SHA256SUMS.txt](SHA256SUMS.txt). The digest of that file is:

```
65c59eaa80992a2c26db74535d15e6533df728b176841fdebf28e4941b62dc96
```

## Scope

The chat-log bundles are not part of this public commitment for now. They are covered by hashes inside the methodology reports, and they will be added here later. An earlier version of this page also listed the chat-log bundles and a hash-chain root for the working log; those were taken out of the public commitment on 27 October 2026, and the earlier version stays in the repository history.

## If a file changes

If any of these files changes before the deadline, this page is updated in a new commit and the earlier version stays in the repository history. The version that matches what was finally uploaded is the one that counts. The three methodology reports were corrected on 27 October 2026 (a factual correction to the description of the agent's memory at the moment it was assembled, and an added paragraph on the agent being a summoned instance); the digests above are the corrected ones.

## How to check, after release

```
sha256sum -c SHA256SUMS.txt
```

run in a folder that holds the released files under the same names.
