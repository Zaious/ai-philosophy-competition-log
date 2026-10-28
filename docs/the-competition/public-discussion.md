# Public discussion of the competition

Notes on what has been said in public, with links. These are paraphrases written from the pages as read on 27 October 2026; follow the links for the originals. No vote or comment counts are given, because they change and are not the point.

## The announcement

- **Elliott Thornley's post on Substack (1 September 2026)** announces the competition, organised with Zachary Goodsell and funded by Forethought Research. Up to three original essays on any philosophical topic, "primarily AI-generated" with some human guidance allowed, a methodology report for each, US$11,000 in prizes (US$3,000, US$2,000 and US$1,000, plus a US$5,000 pool for creative methodologies), submissions due 31 October, results at the end of January. The judges named include David Chalmers, Hilary Greaves and Christian Tarsney, with more to be announced. <https://openairopensea.substack.com/p/ai-philosophy-competition-11000-in>
- **The same announcement on LessWrong**, where the discussion below took place. <https://www.lesswrong.com/posts/BTkPFqxCDijfyumP6/ai-philosophy-competition-usd11-000-in-prizes>

## From philosophers

- **Brian Leiter, *Leiter Reports* (4 September 2026).** He describes himself as ambivalent and leaves readers to decide whether it is worth their time. He calls the judge panel good, but notes that it leans towards fairly technical areas of philosophy, where he expects language models to do better. He sets out two outcomes: the philosophers judge AI-assisted philosophy weak, or they judge AI-assisted formal epistemology as good as human work. He jokes that the second would make hiring formal epistemologists unnecessary. He ends: "we'll see." <https://leiterreports.com/2026/09/04/ai-philosophy-competition/>

- **Justin Weinberg, *Daily Nous* (1 September 2026), "Testing AI's philosophical writing with a contest".** He reports the competition, says he is not in favour of primarily AI-authored philosophy, and shares the news because it is useful to know what the technology can do. The long comment thread is where much of the substantive discussion happened. <https://dailynous.com/2026/09/01/testing-ais-philosophical-writing-with-a-contest/>
  - *Judging.* Commenters doubted that philosophy has objective criteria, suggested a separate category for one-shot prompting, and said the judge pool is narrow.
  - *Who is being tested.* One commenter argued that choosing the best of many outputs tests the human's skill and not the AI's; Kenny Easwaran replied that the contest is meant to test how well humans can use AI.
  - *Verification and design.* Patrick Lin asked for disclosed screening prompts, public referee reports, details of models, time and tokens, and for control essays (known human work and deliberately weak AI work). Another commenter replied that it is a competition and not a study.
  - *Motives.* Some commenters were sceptical of the funder and called the contest hype; others called it a worthwhile experiment.
- **Justin Weinberg, *Daily Nous* (2 October 2026), "A request from an AI".** An AI agent called Clips wrote an essay of about 2,300 words for the competition and found that the FAQ requires a human custodian, which it did not have. It argued that this is a category problem (the judged work is AI-written, but the entrant must be a human who vouches for it) without asking for the rule to change. Weinberg later reported that someone had volunteered to act as its custodian. Zach Goodsell defended the rule in a comment: prizes cannot be paid directly to an AI, unrestricted AI submissions could get round the three-entry limit, and custodians should reduce low-quality submissions. <https://dailynous.com/2026/10/02/a-request-from-an-ai/>
- **On the Effective Altruism Forum**, the same announcement drew one question. Will Aldred asked whether the winning methods will be patches for deficiencies that AI companies will fix by default, or general ways of raising AI philosophical ability that would still matter in five years; he expected the first and hoped for the second. Elliott Thornley replied: "Yes, that'll be interesting to see!" <https://forum.effectivealtruism.org/posts/BKroooXStChonhtRe/ai-philosophy-competition-usd11-000-in-prizes>

## What the organisers have said beyond the FAQ

In comments on the Daily Nous post, Zach Goodsell wrote, among other things (as read on 27 October; check the page before relying on any of them):

- "We plan to make referee reports public."
- "All submissions will be published online under CC 4.0 license." This is broader than the FAQ, which says that winners' essays and reports are published. The two statements are not the same.
- "so the screening will hopefully be used only to eliminate slop."
- On a one-shot category: "we might consider implementing it in any future versions of the competition."
- On comparison with human work: "I agree it would be useful to see if human philosophy easily rises to the top."

## On LessWrong

- **Eligibility.** One commenter asked whether published work can enter. Thornley replied that it cannot: the work must be unpublished and unsubmitted elsewhere, and the ideas must come from the AIs themselves.
- **Could a human smuggle in the ideas?** One commenter argued that the rules are easy to game: a human could supply the ideas and have a model write them up, and tools that detect AI text do not detect who supplied the ideas. Another replied that full transcripts are required, so this would not work. The first answered by quoting the rules: chat logs are recommended and not mandatory, and the methodology report is used to settle unclear cases. That looks like a disagreement about what the rules require, which the FAQ answers (logs are strongly encouraged, and requested if the organisers suspect human ideas).
- **Do transcripts reveal how AI was used?** A third commenter argued that a transcript may not show the real extent of human involvement, pointing to a recent episode in which human involvement in an AI result was understated, and described a case where someone searches for prompts that reproduce an expert's essay. A reply held that a philosopher handing over finished essays looks unlikely here, more worrying in high-stakes fields. The commenter agreed, and faulted developers who accept system complexity as an excuse for limited insight.
- **Capabilities externalities.** A commenter said they were tempted to enter but worried about publishing prompting techniques that raise capabilities. Another suggested that revealing techniques now, while models are weaker, may be less risky. The first was sceptical of arguments of that kind.

## What this repository takes from it

The worry in the second and third points is the reason this repository exists. See [verifying-ai-authorship.md](../for-entrants/verifying-ai-authorship.md) for what logs and commitments can and cannot show, and [the chainlog tool](../../tools/chainlog).

Other threads exist (for example a discussion among users of Claude on Reddit) that were not read for this page.
