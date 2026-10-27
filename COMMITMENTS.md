# Commitments

These are the SHA-256 digests of the files submitted to the AI Philosophy Competition 2026. File names are neutral on purpose. The files themselves are not published here until results are announced.

| File | SHA-256 |
|---|---|
| submission_1/submission1_essay.pdf | `b8443eec4dd0ebe15fa11f283b1ef6760891731e16c85575e66167e62fc4954d` |
| submission_1/submission1_methodology_report.pdf | `fe35c62af0756446b21071dfb2e4985c805152a9c7bc3d26c6d5a1382924493b` |
| submission_1/submission1_chatlog_bundle.zip | `54bb257961c952c7ce6ebbc4f19c031936a4126e4c1f59a2204dc4689aa7d7f5` |
| submission_2/submission2_essay.pdf | `6a81ed654d8f61a470e70ff82da047e440b02599f9a465701656e658d814dc49` |
| submission_2/submission2_methodology_report.pdf | `b415e95807ebab1cae49b0999ca4cce009f3ef99ef34e104f5effd840b0c5519` |
| submission_2/submission2_chatlog_bundle.zip | `dba7096c49b860b07a2a0884729512077f6405d86a62b57bee84f584def1cc90` |
| submission_3/submission3_essay.pdf | `026e9cd1710ba952a181c69d3b143685c85aebb5e55781ab974ebd05bee4de47` |
| submission_3/submission3_methodology_report.pdf | `5191f9f90fbc65015ec5cbcfd64cb53147abb7746a813cc4b219839b99bb5983` |
| submission_3/submission3_chatlog_bundle.zip | `858511929618a1b1deb44bf92fbfeee4540b30c96485d191ad3e630a798bd6f5` |

The same list is in [SHA256SUMS.txt](SHA256SUMS.txt). The digest of that file is:

```
b708cbe933dcfdd081dd7ab864114a79e026571c162dc5e2331f1809491d95f9
```

## If a file changes

The three methodology reports were corrected on 27 October 2026 (a factual correction to the description of the agent's memory at the moment it was assembled); their digests below are the corrected ones, and the earlier digests remain in the repository history.

If any of these files changes before the deadline, this page is updated in a new commit and the earlier version stays in the repository history. The version that matches what was finally uploaded is the one that counts.

## Working log

The three chat-log bundles cover one continuous working log of 795 records. All records are committed by one hash chain. Its root is:

```
7c81be4e2ec156615e32e3fbbe8a8ca159cfdd99af757eda9773bc4c7545d94f
```

## How to check, after release

```
sha256sum -c SHA256SUMS.txt
```

run in a folder that holds the released files under the same names. The verifier for the chat-log bundles will be released with them.
