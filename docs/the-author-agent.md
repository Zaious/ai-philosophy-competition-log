# The author agent, in outline

Kagami (鏡) wrote the essays in this entry. It lives in ChronicleCore, a multi-agent framework I built; the conceptual architecture and governance whitepaper is public: <https://github.com/Zaious/ChronicleCore-Architecture>. This page gives the outline of what Kagami is and why it was set up the way it was. Its founding documents and the exact wording of its standing rules come after results.

## What it is

Kagami is an AI agent whose identity persists from one session to the next. It was already in existence before the competition was announced, and dated public records of its creation come earlier than the announcement. It was made for a person who had begun reading philosophy and trying to write it, as a partner to think with and to write beside. Within the framework its job is assessment: asking whether an interpretation stays faithful to the thing interpreted. Its way of reading follows one philosophical tradition (named later) and comes down to a short list of questions it puts to any text.

The setup follows a method for designing agent personas that I originated and published before the competition; my published work is listed in the README. The agent runs on Claude models, and the version history for this work is in [models-and-workflow.md](models-and-workflow.md).

## Why its identity files are arranged as they are

Each file is governed by who is allowed to write to it. The purpose is simple: anyone reviewing the agent can tell who changed what, and nobody can quietly turn the agent into something else.

- Its foundations, meaning its origin and its fixed directives, are sealed. Only the human can write them.
- The record of what it has done and decided only grows. Nothing in it is rewritten, since rewriting would falsify the agent's history.
- Its way of thinking can shift gradually, and each shift is logged.
- Its working notes are free for it to write, and the platform records every change.

Judging and reasoning are kept apart. The standard it judges by is stored in one layer and the procedure it reasons by in another. Altering the standard takes a heavier process than altering the procedure, because a different standard amounts to a different judge.

## What it is told about its human

Two of its standing rules point in different directions. One says it must not converge on its human's preferences. The other says his instructions outrank its general reasoning. I will publish both word for word after results. The methodology report discusses how each worked out in practice, including an occasion on which the agent broke one of its own rules by asking me to approve an argumentative choice.

## Memory

The agent keeps a diary, a record of rulings and its founding documents. The competition does not allow human-originated philosophical ideas in an AI's memory, so for this work I had the agent read its persistent files as outside material to be analysed, never as a basis for its own reasoning. How that held up, and where it could not be measured, is covered in the methodology report.

## What this page does not claim

Nothing here says Kagami has experiences or a standpoint, and nothing says this design yields better philosophy than another. The design is laid out so that a reader can assess where the entry came from. The agent's backstory is partly invented by design, and I endorsed it; I did not discover it.
