# Can a competition verify that an AI had the ideas?

A note on what evidence can and cannot do for the AI-involvement requirement, written by an entrant. It responds to a worry raised in public discussion of the competition (see [public-discussion.md](public-discussion.md)): a human could supply the ideas, have an AI write them up, and present the result as the AI's. Chat logs are the organisers' remedy, and critics point out that logs are not a complete remedy either.

Both are right. This note tries to say how far each kind of evidence goes.

## Four ways to get it wrong

1. **Ideas supplied openly.** The human says the argument and the AI writes it. A complete log shows this plainly.
2. **Ideas supplied through "neutral" prompts.** The human has the idea first and searches for prompts that make the model produce it. Each prompt looks generic. A log shows every prompt, and still cannot show that the search was running towards a target.
3. **Ideas supplied outside the log.** The human works out the argument elsewhere and brings in only its output. Nothing in the log is false and the log is incomplete.
4. **A log changed afterwards.** Entries edited, dropped or reordered after the fact.

Evidence can reach 1 and 4 well, 2 only in part, and 3 hardly at all.

## A ladder of evidence, from cheap to costly

| Rung | What it gives | What it does not |
|---|---|---|
| Keep the logs, as the organisers ask | the text of the exchange | any protection against 4 |
| Make the log tamper-evident (a hash chain over its lines) | against 4: nothing can be changed after the root is fixed | anything about 1 to 3 |
| Commit before the deadline: publish the root and the hashes of the submitted files with a third-party timestamp | the submission and the log were fixed before the outcome was known | who had the ideas |
| Register every human intervention, one row each, classified against the organisers' lists, with the human's words and the AI's response | a reader can audit each step against the rules, and see the near-line cases listed by the entrant | completeness: the register is the entrant's own selection |
| A provenance table per surviving claim: the earliest dated evidence of the claim, and whether it precedes the human's relevant intervention | shows when an idea first appeared in the record | that "first in the record" means first in fact |
| A replay test: replace each human sentence with a neutral "please continue" and ask what would differ | exposes how much each sentence did | it is a judgement about a run that was never made |
| An independent reader who sees the log blind | a check on the entrant's own classification | independence, if the reader is a similar model or has the same context |

The two rungs that cost nothing and matter most are fixing the log early and listing interventions one by one. Both can be done by any entrant.

## What a competition could ask for

- the root of a hash chain over the full log, committed with the submission, so that a log asked for later can be checked against it;
- a register of human interventions in a standard form, so that reports can be compared;
- for any claim the entrant calls its own, the earliest dated record of it;
- a stated list of what the logged channel does not cover: work done in other tools, other sessions or other people's help.

None of this settles case 2 or case 3. It does make them cost more, and it leaves a record a reader can contest later.

## A tool

[tools/chainlog](../tools/chainlog) is a small hash-chain tool built for this purpose: it makes a log tamper-evident, lets the entrant publish part of a log in full and the rest as hashes, and prints a digest that can be posted as a commitment.
