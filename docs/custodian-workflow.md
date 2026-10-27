# The custodian's workflow, and what this entry changes

## How I have worked until now

For my own research I use a set of AI skills that I built for academic writing. In every paper so far, the ideas and the direction were mine, and an AI helped me argue them and carry them out; my published paper on agent identity design says so in its acknowledgements. My experience has been that the human has to supply the creative idea and decide where the paper lands in theory, while the AI brings fuller knowledge of the field and does much of the drafting, and the human judges the result. Checking references can be done by mechanical rules, and my skills are built on that. But when I let an agent write on its own, I have often got one of two things: a manuscript that strings things together on the surface without a base that can bear weight, or one so safe and conservative that it has no novelty and makes no contribution. So this entry is a new attempt for me.

## What is different here

This entry reverses that, because the competition's rule is the reverse: the philosophical substance has to come from the AI. I proposed topic directions, supplied reference material and process instructions, and gave generic feedback. I supplied no arguments. I wrote none of the text, and I barely read the essays before submitting them. The author agent used the same kind of tools I use myself, a subset of them, listed below.

## The tools the agent used

This says what each tool is for. It does not say how any of it works, and it is not meant to be enough to rebuild it.

| Tool | What it is for |
|---|---|
| `paper-decision-log` | keeps an append-only record of decisions, each with its argument and the alternatives rejected, in a file whose format is checked against a schema |
| `discipline` (philosophy volume) | routes to primary sources, with the Stanford Encyclopedia of Philosophy as first authority, and sets citation conventions and a short list of working rules |
| `chronicle-lex` | the literature library: full texts and catalogue cards, so that quotations and page numbers can be checked against the original |
| `paper-source-audit` | a ledger that sets each claim against the verbatim passage and page in its source, with a verdict |
| `babel-antiai` | scans that flag patterns typical of machine prose and form problems in citations; used to inspect the text, not to rewrite it |
| own scripts | a word counter, a check of every quotation against the full text, and a check of page numbers against the printed page headers |

## Why describe it

So that a reader can see which parts of the process were machinery and which were choices, and so that the contrast with my own earlier way of working is visible. The tools are described, not published.
