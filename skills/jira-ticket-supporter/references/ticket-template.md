# Reader-first Jira writing

Apply these rules to tickets and comments, including input from other skills. Write for colleagues who have not seen the chat. Tell the work's story: the situation, why it matters, what changes, and what remains. Preserve material requirements without reproducing the investigation or implementation record.

## Title and description

For a non-Epic summary use `App or Project - Clear outcome`. Use the real display name and a specific action or result. Do not add internal requirement IDs, classification labels, or unexplained codes. For Epics use [epic-standard.md](epic-standard.md).

Start with a connected narrative of two to four sentences, usually one paragraph. Name the actual people, workflow or product affected; explain the friction and useful change in ordinary language. Use only supported facts. A story is a causal explanation, not fictional scenes, invented user pain, a chronology of agent activity, or a mandatory “As a user” formula.

Then give concise acceptance criteria. The default shape is:

```text
Two to four connected sentences explaining the situation and change.

Acceptance Criteria
- A short, observable outcome.
- Another distinct outcome or consequential exception.
```

An Overview heading is optional. For completed or cancelled work, let the opening tell what happened and what remains; retain the actual acceptance contract without presenting old proposals as active work. Add a separate Outcome paragraph only when it adds information that the opening does not already give, or when a narrowly authorized resolution edit needs it. Do not imply deployment, business acceptance, or resolution from implementation alone. Investigation tickets describe the question and expected findings, not a promised fix.

### Publication limits

| Content | Aim for | Maximum |
| --- | --- | --- |
| Entire description | 120–180 words; less for simple work | 250 words |
| Acceptance criteria | 3–5 distinct outcomes; fewer when sufficient | 5 criteria, 30 words each |
| Each comment | 30–80 words; less for a simple update | 100 words |

Count all visible text, including headings, lists, tables, outcome paragraphs and link labels; exclude the separately managed title and hidden link destinations. These are ceilings, not quotas. Count before publication rather than estimating by appearance. They apply to Epics too; an Epic summarizes its outcome rather than copying child specifications. An explicit user-requested format or length overrides these defaults. “Complex” alone is not an exception.

### Acceptance criteria define success

Each criterion describes one observable outcome in one short sentence. Group tightly related examples only when they share the same pass/fail condition. Keep business thresholds, failure behavior and access boundaries that determine correctness. A compact rule table may clarify a real decision rule within the total word limit; it must not conceal extra criteria.

Do not turn ACs into implementation steps, resource/file inventories, deployment recipes, exhaustive test matrices or generic instructions to test, review, document and follow the workflow. Include such a deliverable only when it is specifically part of the requested outcome. Do not restate the same rule as both a requirement and a list of tests. Do not meet the count limit by packing unrelated obligations into long sentences, semicolon chains or nested lists. Avoid vague replacements such as “all edge cases work.”

### If the draft is too long

Redraft before publishing. State each fact once, remove superseded alternatives from the current description, and replace repeated implementation/verification detail with the outcome it establishes. Preserve important dates, eligibility rules, authorization boundaries and unresolved blockers inline. The ticket must explain the work and its acceptance without requiring another link.

Supporting implementation detail, exact test cases and operational procedures can remain in an existing maintained specification, runbook or verification record, with one descriptive link when useful. Verify that the record actually contains the necessary detail and is suitable for the intended readers; a private local artifact or invented link is not a substitute. Do not remove a genuinely required constraint merely because it sounds technical. Do not move overflow into a giant comment, appendix or another ticket, and do not create a separate guide as a routine workaround.

If distinct essential requirements still cannot fit, preserve the complete draft locally and identify the specific conflict. Resolve only the necessary scope/format choice before publishing that draft, such as explicit permission for a longer description. Continue independent work. Never silently exceed the limit, truncate requirements, or split tickets without authorization.

For a narrow edit to an existing long ticket, constrain the new/revised passage and preserve the authorized edit boundary; the length rule does not authorize rewriting unrelated content or block the requested small correction. For authorized historical-comment cleanup, preserve the knowledge and decisions at that time. If safe shortening is impossible, leave that comment intact and report the exception rather than erasing its substance.

Do not add separate Problem, If we skip it, empty Fix, Implementation Classification, or Definition of Done sections by default. Integrate their useful meaning into the overview or criteria once. A distinct completion requirement belongs in a criterion. Do not require PRs, code changes, deployment, or documentation for work that does not need them.

### Fictional example: a short story with clear acceptance

Resource Portal users need Excel workbooks without converting CSV files. This change adds Excel alongside CSV across the export workflow, so people can choose the format they need. The implementation is verified locally and ready for review.

**Acceptance Criteria**
- Resource, saved-report and inventory-summary exports offer both Excel and CSV.
- Downloads contain only permitted rows for the active filters, selected reports and completed inventory runs.
- Column labels and literal cell values remain unchanged.
- Filtered and unfiltered Excel workbooks open without repair or corruption warnings.

Use the example's connected explanation and brevity, not its application-specific facts, as the pattern.

## Context without clutter

Explain a requirement in words before considering a source link. Replace “R6 / row 3” with “Show Complete for completed training, including GDPR.” If an improvement's relationship matters, say what it is and why this ticket contributes. There is no mandatory “Belongs to Improvement(s)” section. Do not infer a requirement from a parent alone.

Include a source or related-work link only when it helps the reader act, understand a dependency, or resolve a real ambiguity. Use a descriptive title and a verified destination. One useful source is better than repeated provenance. Omit the source section entirely when it adds no value. A ticket must remain understandable without opening its links.

- Keep spreadsheet row/column coordinates, transcript offsets, opaque requirement IDs, comment IDs, execution/run IDs, hashes/SHAs, exact publication timestamps, test totals, local file paths, and raw logs in internal evidence or the relevant technical artifact. Do not copy them into routine tickets or comments.
- Retain exact dates, times/timezones, thresholds, technical identifiers, or versions **when they define required behavior, a contractual interface, a reproducible defect, or a consequential decision**. Explain their meaning. A training cutoff date belongs; the timestamp when an agent inspected it usually does not.
- PR and commit references belong in the development system by default. Include a named PR link only when the reader must review it or it is an actual blocker/decision in this ticket; omit bare PR numbers and repeated commit hashes.
- Do not expose the author's private skill names, agent roles, tool output, delegation chain, review labels such as “Ship,” or instruction names as evidence or acceptance criteria. Translate to the work outcome. When the ticket itself explicitly concerns maintaining or distributing skills, name the actual skill deliverables that readers need; do not remove the subject of the work.
- Avoid implementation plans, file inventories, schema dumps, and speculative architecture in ordinary tickets. Keep a technical constraint if omitting it would change the requested outcome, security, data preservation, or integration contract. Use the smallest explanation needed by the intended assignee.
- Keep sensitive personal data and secrets out. Use sanitized examples when examples are necessary.

For chat drafts, use Markdown links with descriptive labels. In Jira ADF, create a native link mark on descriptive text. Never embed `[label](url)` or `[label|url]` as literal ADF text. If only plain text is supported, use a descriptive label followed by the URL on its own line, only when useful; avoid glued-on punctuation. Do not invent missing URLs or claim that readers have access unless verified.

## Comments

A comment is an update, not another ticket. Default to one short paragraph of two to four sentences, or a few short bullets when easier to read, within the limits above. No mandatory headings or checklist. Give the change or finding, its consequence, and the next step or remaining blocker once. Do not turn it into a complete technical handoff.

Say what changed or was found, its consequence for the requested outcome, and what remains or needs a decision. Only include new information. Skip ceremonial “Work started” comments or empty “Follow-ups: none” fields when the status already conveys that fact. For a shared release, describe this ticket's result rather than copying the same release report to every related ticket. Clearly distinguish implemented, reviewed, deployed, validated with real users/data, and accepted. Preserve failed/blocked checks that affect readiness, without dumping successful test counts or review machinery. A source link is optional under the same usefulness test as descriptions.

Example update:

“Completed training now displays Complete consistently, including GDPR. Checks confirm that incomplete and overdue values still behave as before. The change is ready for deployment; it is not live yet.”

Example blocker:

“The import is ready for UAT validation. Existing records will be preserved, and conflicting rows will be rejected. Production import remains on hold until UAT is accepted and Production approval is given.”

Do not append a new narrative to a description just to record progress when the requested action is a comment. Do not edit old comments to erase history without authorization. During an authorized description revision, make the current requirement consistent instead of retaining superseded instructions as active scope.

## Final reader check

Count the description, criteria and comment words against the limits. Then read for meaning: can a colleague retell the situation, change and remaining action after one read? Does each criterion have one clear pass/fail outcome? Is a fact repeated across the story, ACs and outcome? Are tentative facts and important limits visible? Does every retained number, technical term and link help the reader understand or act? A passing word count cannot compensate for dense prose, missing requirements or a disconnected story.
