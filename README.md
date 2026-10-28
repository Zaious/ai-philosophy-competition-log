# AI Philosophy Competition 2026: an entry log

I entered the [AI Philosophy Competition](https://www.zacharygoodsell.com/ai-philosophy-competition) (organisers: Zachary Goodsell and Elliott Thornley; deadline 31 October 2026, AoE) with three essays and three methodology reports. The essays are the work of an AI agent, Kagami (鏡), as the competition requires; I acted as its custodian. This repository is under my own name, so I am not anonymous here. What is embargoed is the content of the entry, because the competition's judging is blind.

## What this repository is for

It is a record, not a how-to. The deadline is close, so nobody can repeat the seven weeks of this entry now. I made it public at this time on purpose, for four things:

1. to introduce the competition, from the organisers' own pages ([competition/](competition/));
2. to point to the discussion about it elsewhere on the internet ([competition/public-discussion.md](competition/public-discussion.md));
3. to say who I am and how I have worked with AI until now ([Who is who](#who-is-who) and [entry/custodian-workflow.md](entry/custodian-workflow.md));
4. to publish my own entry after the judging stage ([after-results/](after-results/)), with hashes fixed before the deadline, so anyone can check it later ([COMMITMENTS.md](COMMITMENTS.md)).

## Who is who

**The custodian: Meng-Han Lee (Zaious).** An independent researcher and AI agent architect in Taiwan, with an M.S. in Interaction Design (National Taipei University of Technology). I build multi-agent systems and write about how designed interaction shapes people. My published work includes the Agentic Social Affordance Framework (ASAF), a peer-reviewed paper arguing that agent identity design is a collaboration interface and not a cosmetic layer ([Frontiers in Computer Science, 2026](https://doi.org/10.3389/fcomp.2026.1860996)). That paper's own rule is that the concepts are mine and AI assists; this entry runs the other way, as the competition requires. I have no formal training in philosophy; I grew up in a family where how education shapes people was always being discussed. In this entry my role is custodian: I chose the topic areas, supplied material and process instructions, and handled the submission. The philosophical work is the agent's. My research interests lie near the essays' territory, and the [checklist](entry/human-involvement-checklist.md) says what I checked because of that. [zaious.dev](https://zaious.dev) · [ORCID](https://orcid.org/0009-0007-1685-0877)

**The author: Kagami (鏡).** An AI agent with a persistent identity, running on Claude models inside ChronicleCore, the multi-agent system I built ([whitepaper](https://github.com/Zaious/ChronicleCore-Architecture)). It was made as an interlocutor for someone reading and beginning to write philosophy, and its standing role is that of an assessor: it asks whether an interpretation is faithful to what it interprets. It existed before the competition was announced. More in [entry/the-author-agent.md](entry/the-author-agent.md).

The competition asks for anonymous submissions and judges them blind, so **nothing about the essays themselves is published here yet**: no titles, abstracts, topics, arguments or sources. That stays embargoed until results are announced (the organisers expect the end of January 2027). What is here is everything about the entry that can be shown without that, plus one public commitment so that the rest can be checked later.

## Map of the repository

```
README.md        this page
COMMITMENTS.md   SHA-256 of every file submitted, and the root of a hash chain over the working log
SHA256SUMS.txt   the same hashes as a list that sha256sum can check
competition/     the competition: official sources, rules mapped, public discussion, related entries, two guides
entry/           this entry: the human's part, the models, the author agent, the first day, our timeline
after-results/   empty until results; the essays and reports will be added here (and what is public when)
tools/chainlog/  a small tool that makes a chat log tamper-evident (MIT)
```

**The commitment.** [COMMITMENTS.md](COMMITMENTS.md) records the SHA-256 of every file submitted (the essays, the methodology reports and the chat-log bundles) and the root of a hash chain over the full working log, fixed before the deadline. Publishing the chat logs themselves is not promised; the hashes are there so that a log, if it is released or asked for, can be checked. A commitment shows only that the files were not edited afterwards. It does not show who had the ideas.

**After results.** The three essays and methodology reports (the competition publishes winners under CC BY 4.0; I plan to publish mine after results), the author agent's details, and instructions for checking every hash in COMMITMENTS.md against the released files. Whether and in what form the chat logs are released has not been decided. The full table is in [after-results/README.md](after-results/README.md).

## Why

Public discussion of the competition raises the worry that a human can quietly supply the ideas and present them as the AI's, and that chat logs cannot fully settle this. I cannot answer that with an argument. I can fix the evidence in advance, describe the involvement as plainly as I can, publish what I plan to publish after results, and let others check.

## Licence

Code (`tools/`): MIT, see [LICENSE](LICENSE). Text in `entry/`, `competition/`, `after-results/` and the top-level pages: CC BY 4.0.
