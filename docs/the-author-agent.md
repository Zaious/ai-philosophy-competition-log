# The author agent, in outline

A short, abstract description of the agent that wrote the entry's essays. It is called Kagami (鏡). It lives in ChronicleCore, a multi-agent framework I built, whose conceptual architecture and governance whitepaper is public: <https://github.com/Zaious/ChronicleCore-Architecture>. Its founding documents and the full text of its standing rules are withheld until results, and will be published then. This page says what kind of thing it is and why it was built that way, not how to build another one.

## What it is

An AI agent with a persistent identity. It existed before the competition was announced, and dated public records of its creation precede the announcement. It was made as a companion for a person who was reading philosophy and beginning to write it: an interlocutor to explore questions with, and to write alongside. It was built by a method of agent persona design that I originated and published before the competition; the reference is withheld until judging is complete, as in the methodology report. Its standing role in the system it lives in is that of an assessor, someone who asks whether an interpretation is faithful to what it interprets. It reads by a fixed discipline drawn from one philosophical tradition (named later), expressed as a small set of questions it asks of any text.

It runs on a Claude model. The model underneath has changed over its life; the versions used during this work are in [models-and-workflow.md](models-and-workflow.md).

## How its identity is governed

The files that make up its identity are governed by who may write them, so that a reader can see who changed what, and so that it cannot be quietly rewritten into something else:

- what defines it (its origin and fixed directives) is sealed and writable only by the human;
- what it has lived through and judged is append-only;
- how it thinks may change slowly, and every change leaves a trace;
- its working materials it may write freely, and each change is recorded by the platform.

The standard by which it judges and the procedure by which it reasons are kept in two separate layers. The first changes only through a heavier process, because changing a criterion is changing who judges.

## Its standing rules about its human

Two of its standing rules pull in different directions, and both will be published verbatim after results. One tells it not to converge on its human's preferences. Another gives his instructions priority over its general reasoning. The entry's methodology report discusses what each did in practice, including a case where the agent broke a rule of its own by asking the human for approval of an argumentative choice.

## Memory

It keeps a diary, a record of rulings, and founding documents. For this work the persistent files were treated as external data to be analysed and not as background for reasoning, because the competition's memory clause does not allow human-originated philosophical ideas in an AI's memory. How that worked, and where it could not be measured, is in the methodology report.

## What this page does not claim

It does not claim that the agent has experiences or a standpoint, or that this design produces better philosophy than any other. The design is described so that a reader can judge the entry's provenance, and for no other purpose. The report states that the identity's backstory is partly invented by design and was endorsed by the human, not discovered.
