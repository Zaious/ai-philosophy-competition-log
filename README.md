# AI Philosophy Competition 2026: an entry log

I entered the [AI Philosophy Competition](https://www.zacharygoodsell.com/ai-philosophy-competition) (organisers: Zachary Goodsell and Elliott Thornley; deadline 31 October 2026, AoE) with three essays and three methodology reports. The essays are the work of an AI agent, Kagami (鏡), as the competition requires; I acted as its custodian. This repository is under my own name, so I am not anonymous here. What is embargoed is the content of the entry, because the competition's judging is blind.

## Where to start

| If you want to | Go to |
|---|---|
| see how much the human did and did not do | [the human-involvement checklist](docs/about-the-entry/human-involvement-checklist.md) |
| know which models were used and what is measured | [models and workflow](docs/about-the-entry/models-and-workflow.md) |
| see how the work went, week by week | [the weekly rhythm](docs/about-the-entry/weekly-rhythm.md) |
| check that the files were not changed afterwards | [COMMITMENTS.md](COMMITMENTS.md) |
| know what is public now and what comes after results | [the release plan](docs/release-plan.md) |
| read the competition's rules and what people said about it | [docs/the-competition/](docs/the-competition/) |
| write your own methodology report, or make a log tamper-evident | [docs/for-entrants/](docs/for-entrants/) and [tools/chainlog](tools/chainlog) |

## Who is who

**The custodian: Meng-Han Lee (Zaious).** An independent researcher and AI agent architect in Taiwan, with an M.S. in Interaction Design (National Taipei University of Technology). I build multi-agent systems and write about how designed interaction shapes people. My published work includes the Agentic Social Affordance Framework (ASAF), a peer-reviewed paper arguing that agent identity design is a collaboration interface and not a cosmetic layer ([Frontiers in Computer Science, 2026](https://doi.org/10.3389/fcomp.2026.1860996)). That paper's own rule is that the concepts are mine and AI assists; this entry runs the other way, as the competition requires. I have no formal training in philosophy; I grew up in a family where how education shapes people was always being discussed. In this entry my role is custodian: I chose the topic areas, supplied material and process instructions, and handled the submission. The philosophical work is the agent's. My research interests lie near the essays' territory, and the [checklist](docs/about-the-entry/human-involvement-checklist.md) says what I checked because of that. [zaious.dev](https://zaious.dev) · [ORCID](https://orcid.org/0009-0007-1685-0877)

**The author: Kagami (鏡).** An AI agent with a persistent identity, running on Claude models inside ChronicleCore, the multi-agent system I built ([whitepaper](https://github.com/Zaious/ChronicleCore-Architecture)). It was made as an interlocutor for someone reading and beginning to write philosophy, and its standing role is that of an assessor: it asks whether an interpretation is faithful to what it interprets. It existed before the competition was announced. More in [docs/about-the-entry/the-author-agent.md](docs/about-the-entry/the-author-agent.md).

The competition asks for anonymous submissions and judges them blind, so **nothing about the essays themselves is published here yet**: no titles, abstracts, topics, arguments or sources. That stays embargoed until results are announced (the organisers expect the end of January 2027). What is here is everything about the entry that can be shown without that, plus one public commitment so that the rest can be checked later.

## Map of the repository

```
README.md            this page
COMMITMENTS.md       SHA-256 of every file submitted, and the root of a hash chain over the working log
SHA256SUMS.txt       the same hashes as a list that sha256sum can check
docs/                everything written about the entry (index: docs/README.md)
  release-plan.md      what is public now, what comes after results, what is not promised
  about-the-entry/     the human's part, the models, the author agent, the first day, the weekly rhythm
  the-competition/     official sources, the rules mapped, public discussion, related entries, dates
  for-entrants/        a checklist for the methodology report, and what logs can and cannot prove
tools/chainlog/      a small tool that makes a chat log tamper-evident (MIT)
released/            empty until results; the essays and reports will be added here
```

**The commitment.** [COMMITMENTS.md](COMMITMENTS.md) records the SHA-256 of every file submitted (the essays, the methodology reports and the chat-log bundles) and the root of a hash chain over the full working log, fixed before the deadline. Publishing the chat logs themselves is not promised; the hashes are there so that a log, if it is released or asked for, can be checked. A commitment shows only that the files were not edited afterwards. It does not show who had the ideas.

**After results.** The three essays and methodology reports (the competition publishes winners under CC BY 4.0; I plan to publish mine after results), the author agent's details, and instructions for checking every hash in COMMITMENTS.md against the released files. Whether and in what form the chat logs are released has not been decided. The full table is in [docs/release-plan.md](docs/release-plan.md).

## Why

Public discussion of the competition raises the worry that a human can quietly supply the ideas and present them as the AI's, and that chat logs cannot fully settle this. I cannot answer that with an argument. I can fix the evidence in advance, describe the involvement as plainly as I can, publish what I plan to publish after results, and let others check.

## Licence

Code (`tools/`): MIT, see [LICENSE](LICENSE). Text in `docs/` and the top-level pages: CC BY 4.0.
