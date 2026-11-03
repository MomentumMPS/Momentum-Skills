# Report template and example

Use this structure for every format (chat, doc, doc plus spreadsheet). Only the length changes.

## Template

```
# What [you / Name] did, [start date] – [end date]

[One paragraph: range, number of evidence items found across N sources, and the themes in one sentence each.]

## [Theme 1 — a name the user would use in a meeting]
[One line: what this is.]
- [date] [action, in plain language] — [source: link / title / meeting name] [(involvement) if level b or c]
- ...
Outcome: [shipped / decided / in review / blocked / handed off, with the evidence that shows it]

## [Theme 2]
...

## Routine and overhead
- [recurring meeting series, attended N of M]
- [triage, reviews, on-call, admin — one line each]

## Gaps
- [source] not connected / returned nothing
- [dates] no evidence found; [reason if known]
- [anything the user should confirm from memory]
```

## Fictional example (short range, chat format)

All names, dates, ticket keys, and events below are illustrative, not user data.

# What you did, Mon Oct 19 – Fri Oct 23, 2026

Five working days, 41 evidence items across Slack, Gmail, Google Calendar, Zoom and Linear. Three themes: the Q4 pricing proposal (most of the week), the onboarding-flow bug triage, and prep for the November customer summit.

## Q4 pricing proposal
Getting the tiered-pricing proposal from draft to leadership review.
- Oct 19 — Shared draft v2 with Dana and Priya for review — Slack #pricing, permalink
- Oct 20 — Pricing sync (45 min, you organized); agreed to drop the "Starter" tier — Zoom summary
- Oct 21 — Rewrote sections 2–4 after the sync; 38 edits — Google Doc "Q4 Pricing Proposal", version history
- Oct 22 — Sent proposal to Marcus with a one-page summary — Gmail, "Q4 pricing: ready for review"
- Oct 23 — Answered Marcus's three questions in thread — Gmail, same thread
Outcome: in leadership review; Marcus replied "will bring to Monday's staff meeting."

## Onboarding-flow bug triage
Handling the spike of signup failures reported Oct 20.
- Oct 20 — Picked up ONB-412 and reproduced the failure — Linear, status → In Progress
- Oct 20 — Posted root cause (expired OAuth config) in #eng-incidents — Slack permalink
- Oct 21 — Closed ONB-412 after Lee's fix shipped; closed duplicate ONB-415 — Linear
Outcome: resolved; two tickets closed.

## Customer summit prep
- Oct 22 — Summit planning meeting, attended — Google Calendar (participated; no transcript)
- Oct 23 — Created "Summit demo script" doc — Google Drive

## Routine and overhead
- Daily standup, 5 of 5
- Weekly 1:1 with Marcus, Oct 21
- Reviewed two of Lee's PRs (links in #eng-reviews)

## Gaps
- Notion not connected; you mentioned keeping meeting notes there.
- No evidence Friday afternoon after 2 pm.
- The Oct 22 summit meeting has no transcript, so your contribution there isn't recorded.
