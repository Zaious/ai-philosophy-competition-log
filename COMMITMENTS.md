# Commitments

These are the SHA-256 digests of the files submitted to the AI Philosophy Competition 2026. File names are neutral on purpose. The files themselves are not published here until results are announced.

| File | SHA-256 |
|---|---|
| submission_1/submission1_essay.pdf | `b8443eec4dd0ebe15fa11f283b1ef6760891731e16c85575e66167e62fc4954d` |
| submission_1/submission1_methodology_report.pdf | `91212f7ac47f5f9e3179c86595dbfb191124957ac0d9cde2e9d8563195d8166c` |
| submission_1/submission1_chatlog_bundle.zip | `54bb257961c952c7ce6ebbc4f19c031936a4126e4c1f59a2204dc4689aa7d7f5` |
| submission_2/submission2_essay.pdf | `6a81ed654d8f61a470e70ff82da047e440b02599f9a465701656e658d814dc49` |
| submission_2/submission2_methodology_report.pdf | `cdf43108fc9f90f66fb08aa1edf9d52b28f32e943fbe56889ca3f8035e1b3cc8` |
| submission_2/submission2_chatlog_bundle.zip | `dba7096c49b860b07a2a0884729512077f6405d86a62b57bee84f584def1cc90` |
| submission_3/submission3_essay.pdf | `026e9cd1710ba952a181c69d3b143685c85aebb5e55781ab974ebd05bee4de47` |
| submission_3/submission3_methodology_report.pdf | `b44c052416d5f9229db92d8080f9c0739229e02ab64803bc65653d75f41a3257` |
| submission_3/submission3_chatlog_bundle.zip | `858511929618a1b1deb44bf92fbfeee4540b30c96485d191ad3e630a798bd6f5` |

The same list is in [SHA256SUMS.txt](SHA256SUMS.txt). The digest of that file is:

```
181cb82cf96d35ede490d0ce638aa5f7afe3f67a8dc76940f71df28afd6afaac
```

## If a file changes

The three methodology reports were corrected on 27 October 2026 (a factual correction to the description of the agent's memory at the moment it was assembled, and an added paragraph on the agent being a summoned instance); their digests below are the corrected ones, and the earlier digests remain in the repository history.

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
