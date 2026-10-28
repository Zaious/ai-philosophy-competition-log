# Writing the methodology report: a checklist from one entrant

The FAQ lists what a report should contain. This checklist adds what the entry's authors found hard in practice. It is not official guidance.

## The FAQ's list, with a note on each

| The FAQ asks for | Practical note |
|---|---|
| Models and versions | Get versions from the session records, not from memory. If a stretch cannot be recovered, write "not measured" and give the nearest indirect record separately, labelled as indirect. |
| Role of each model; what each originated | Say what each model did, and say what it did not do. |
| Prompts, system instructions, tools, scaffolds, architecture | Decide early how much you will show. If you describe only the shape, say so, and say what is withheld. |
| How topic, position or conclusion was selected | Quote the human's wording of the topic if you can. A topic phrased with a presupposition in it is worth flagging yourself. |
| How many candidates were generated | Count them from records and say where the line between "candidate" and "passing thought" is drawn. |
| How outputs were selected, tested, criticised, revised | A table of rounds beats a narrative: target, verdict, what was accepted, what was rejected, what changed. |
| Every form of human involvement | One row per intervention, with the human's words, the effect on content, and the rule item it falls under. List the near-line cases yourself. |
| Memory, retrieval, browsing, tools | If the agent has persistent memory, say what it holds and which items were retrieved into context. Measure it if you can. |
| Human time, machine time, tokens, cost | Separate measured from estimated, always. Give the method and the range for estimates. Human time can be the human's own estimate, labelled so. |
| Automated evaluation or screening | Name the checks that were run and what each found, including false alarms. |
| Chat logs or other records | Decide the form before the last week (see below). |
| Human versus AI actions | Mark the actor in every table. |

## Three things that cost the most time

1. **Session records can disappear.** Claude Code deletes older session transcripts at startup under the setting `cleanupPeriodDays`, whose documented default is 30 days. An entry that runs for more than a month can lose its early sessions. Check the current documentation for your tool, raise the setting at the start of the work, and keep a copy of the transcripts somewhere that is not swept. Whatever platform you use, ask on day one how long it keeps sessions.
2. **Cost and token figures are usually estimates.** Say which are measured. Where a stretch has cost but no per-round record, show the arithmetic.
3. **Redaction has to be decided before upload.** The FAQ says to redact private material before submission, because the report is published. A log with personal passages in it needs a rule for what is left in, what is replaced, and how each replacement is listed.

## What helped to make the report checkable

- A list, in the report, of every claim you cannot support, in the report's own words ("not measured", "I cannot show").
- Hashes of the files submitted and of the log, committed before the deadline (see [verifying-ai-authorship.md](verifying-ai-authorship.md)).
- A rule that nothing in the report is stronger than the record behind it. Re-reading a finished report for sentences that break this rule found errors every time.
