# Models used, and the workflow in outline

Both are taken from the entry's methodology report, with the report's own qualifications kept.

## Models

| Role | Model | How it is known |
|---|---|---|
| Author agent, first sessions (8 September) | `claude-sonnet-5` | measured from the session records |
| Author agent, 8 to 19 September | **not measured**. The platform's configuration file records `claude-sonnet-5` | the session records for these rounds are no longer on disk; the text of the rounds is kept in the platform log |
| Author agent, 4 October onwards | `claude-sonnet-5-5` | measured from the session records |
| Reviewer agent | not recorded; described as an independently configured agent of the same model family | the same-family point is a stated limit: errors may be correlated |
| Drafting of the agent's identity files, before the competition | an earlier pair of models (Fable 5 and Opus 4.8), as relayed from public documentation | not verified; the report says they took no part in writing, reviewing or auditing any essay |

The model underneath the author agent was swapped once at the start of the logged work (a platform notice records it); the earlier conversation history did not carry over. Usage and cost figures in the report are the client's estimates at list prices, not bills; part of them are estimated and marked as such.

## Workflow, in outline

One pass per essay, with the order fixed in advance:

1. **Topic.** The human gives a subject or question, not a thesis.
2. **Position first.** The agent writes one page: its claim, the strongest objection to it, the conditions under which it would give the claim up, and what it expects to find. It does this *without* searching for neighbouring work. Later additions go below the line; the page is not rewritten.
3. **Neighbours and primary texts.** The agent then reads the primary sources in full where it can, checks page numbers against the printed page, and says plainly when only an abstract was read. If the ground is occupied it says so and does not invent a replacement.
4. **Drafting** under the word budget, with net deletions only and every quotation checked against its source.
5. **Adversarial review.** A separate reviewer agent is given the verbatim text and presses objections. The agent checks each objection against the sources before accepting or answering it. The human only opens the consultation.
6. **Audit.** A ledger of sources and claims with the verbatim passage and page for each; a whole-text quotation audit; a style scan; an anonymity scan.
7. **Decision log** throughout: every turning-point decision records its argument and the alternatives rejected.

## Two things the report says about this workflow

- The "position first" order was not in place from the start. It came in after the human reminded the agent of its order of work, and the report says it cannot show that the order made the essays better, because there is no comparison run.
- The adversarial reviewer's share of the final wording is large, and the report says so essay by essay.
