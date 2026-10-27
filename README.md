# AI Philosophy Competition 2026: an entry log

I entered the [AI Philosophy Competition](https://www.zacharygoodsell.com/ai-philosophy-competition) (organisers: Zachary Goodsell and Elliott Thornley; deadline 31 October 2026, AoE) with three essays and three methodology reports. The essays are the work of an AI agent, Kagami (鏡), as the competition requires; I acted as its custodian. This repository is under my own name, so I am not anonymous here. What is embargoed is the content of the entry, because the competition's judging is blind.

The competition asks for anonymous submissions and judges them blind, so **nothing about the essays themselves is published here yet**: no titles, abstracts, topics, arguments or sources. That stays embargoed until results are announced (the organisers expect the end of January 2027). What is here is everything about the entry that can be shown without that, plus one public commitment so that the rest can be checked later.

## What is here now

**The commitment.** [COMMITMENTS.md](COMMITMENTS.md) records the SHA-256 of every file submitted and the root of a hash chain over the full working log, fixed before the deadline. A commitment shows only that the files were not edited afterwards. It does not show who had the ideas.

**About the entry**
- [docs/human-involvement-checklist.md](docs/human-involvement-checklist.md): how much the human did and did not do, item by item against the organisers' lists of permitted and forbidden involvement.
- [docs/models-and-workflow.md](docs/models-and-workflow.md): which models, with what is and is not measured, and the workflow in outline.
- [docs/the-author-agent.md](docs/the-author-agent.md): the author agent described in outline; founding documents and rule text after results.
- [docs/day-one-notes.md](docs/day-one-notes.md): the first day's discussion of the competition, de-identified.

**About the competition**
- [docs/rules-map.md](docs/rules-map.md): the rules and FAQ mapped, including the rules that are easy to miss and the questions the pages leave open.
- [docs/public-discussion.md](docs/public-discussion.md): what has been said in public, with links.
- [docs/timeline.md](docs/timeline.md): dates.

**For other entrants**
- [docs/methodology-report-guide.md](docs/methodology-report-guide.md): a checklist from one entrant, including a way to lose your own session records.
- [docs/verifying-ai-authorship.md](docs/verifying-ai-authorship.md): what logs and commitments can and cannot prove about who had the ideas.
- [tools/chainlog](tools/chainlog): a small tool (Python, standard library only, with tests and a demo) that makes a chat log tamper-evident and lets you publish part of a log in full and the rest as hashes.

## What will be released after results

The three essays and methodology reports (the competition publishes winners under CC BY 4.0; I plan to publish mine after results), the chat-log bundles with their verifier (the full working conversation, Chinese original with English translation), the author agent's details, and instructions for checking every hash in COMMITMENTS.md against the released files.

## Why

Public discussion of the competition raises the worry that a human can quietly supply the ideas and present them as the AI's, and that chat logs cannot fully settle this. I cannot answer that with an argument. I can fix the evidence in advance, describe the involvement as plainly as I can, publish everything later, and let others check.

## Licence

Code (`tools/`): MIT, see [LICENSE](LICENSE). Text in `docs/` and the top-level pages: CC BY 4.0.
