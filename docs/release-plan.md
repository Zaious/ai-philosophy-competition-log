# What is public now, what comes later, what is not promised

The competition judges blind, so the content of the entry is embargoed until results. This page fixes in advance which part of the repository is open now, what is planned for release after results, and what is not promised. A plan is not a commitment; the hashes in [COMMITMENTS.md](../COMMITMENTS.md) are.

| Status | What | Where |
|---|---|---|
| **Public now** | this repository's pages: who is who, the human-involvement checklist, models and workflow, the custodian's workflow, the author agent in outline, the rules map, official sources, public discussion, related entries, timeline, the weekly rhythm, the guides for other entrants | `README.md`, `docs/` |
| **Public now** | the commitments: SHA-256 of every file submitted, and the root of a hash chain over the working log | `COMMITMENTS.md`, `SHA256SUMS.txt` |
| **Public now** | a tool for making a chat log tamper-evident (MIT licence) | `tools/chainlog/` |
| **Planned after results** | the three essays and the three methodology reports, under the same file names as in `SHA256SUMS.txt`. The competition publishes winning entries under CC BY 4.0; I plan to publish mine after results | `entry/` (empty until then) |
| **Planned after results** | the author agent's founding documents and its two standing rules, word for word | to be added, with a page in `docs/` |
| **Planned after results** | instructions for checking each released file against its hash | `entry/README.md` |
| **Not decided** | the chat logs themselves, and in what form. The hashes are public so that a log, if it is released or asked for, can be checked | none |
| **Not published** | how the tools and the agent work internally, prompts, and private material. They are described in outline, not published | none |

## How the line is kept

- Nothing about the essays' titles, abstracts, topics, arguments or sources is placed in `docs/`. Pages here describe the process and the evidence, not the content.
- Released files go in the folder `entry/` and nowhere else, so that what was added after results is visible in the repository history.
- Pages in `docs/` are not moved or renamed, so links to them keep working.
- If a planned item changes, this page is updated in a new commit, and the earlier version stays in the history.

## Dates

The organisers expect results at the end of January 2027. Release follows the announcement; see [timeline.md](timeline.md).
