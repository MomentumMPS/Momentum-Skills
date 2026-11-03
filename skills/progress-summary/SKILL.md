---
name: progress-summary
description: Use work-detective to research the reporting week, then write the user's 2–3 minute spoken leadership update for their chosen audience, with bold Regarding topic labels and natural narrative bullets. Use for Friday updates, weekly leadership progress, or revisions of that speaking script.
---

# Weekly leadership narrative

Prepare a casual, credible update the user can deliver to their chosen audience in 2–3 minutes. Show modest leadership through evidenced ownership, delivery, coordination, and clear status. Use complete spoken sentences in unordered lists grouped by application or initiative.

## Research through work-detective

Read and use [work-detective](../work-detective/SKILL.md) for intake, source inventory, evidence collection, cross-checking, and the cited case file. Resolve that dependency relative to this skill's real installation directory, so both skills remain siblings regardless of the global installation location. If unavailable, search the skill catalog before reporting the missing dependency; do not substitute a shallower search silently.

For a new reporting period:

- Honor supplied dates. For “this week” or an unspecified Friday update, use Monday through Friday of the current reporting week in the user's timezone, capped at the actual collection cutoff. Resolve the timezone from trusted current user or host context; ask if unavailable. State the explicit dates and cutoff in the research context; never imply future events have happened.
- Resolve audience, purpose, language, and email provider from the current request or trusted user context. Use the conversation language unless another is requested. Work-detective owns intake: resolve the involvement level and missing email choice for a new investigation; do not re-ask answers already provided for this case. Do not assume a previous user's preferences.
- Follow work-detective's broad source coverage, authored and participation passes, pagination, cross-source leads, privacy boundaries, and missing-access handling. Preserve dates, links, and authored/participated/looped-in labels in `evidence.md` in a report-specific working folder. An empty result is not an inaccessible source.
- Verify the current user's identity before attributing work; use available connectors before CLI or UI fallbacks, following the host's execution and approval rules.

This skill controls the final presentation. Work-detective's detailed report, evidence counts, citations, and involvement labels are supporting material, not text the user must read aloud. Keep its research rigor without reproducing its full report in the speaking script.

## Choose the content and attribute it

Group by real applications or initiatives. Features belong under their parent application: reminders in a training portal remain part of that topic. Combine small intake/handoff topics when useful; do not force exactly three topics or reuse last week's application names without current evidence.

Lead with delivered outcomes, then meaningful progress, owner requests, and material remaining work. Keep substantive coordination and early project context when supported; describe receiving context as receiving context. Leave routine attendance and activity counts out of the script.

- Use **“I”** for the user's own implementation, investigation, decisions, organization, communication, and coordination. Use “we” only for a genuinely joint result. “I coordinated with the application owners after a colleague's integration fix” preserves both leadership and credit. Never imply the user implemented a colleague's fix or manages them.
- Explain owner needs naturally: “They wanted X” or “They requested X because Y.” Name the owner/team first when the antecedent is unclear. Include a reason only if evidenced or supplied by the user. Distinguish the owner's request from the user's proposed implementation: “They wanted daily reports, so I defined an approach that reuses existing coordinates.”
- Give the audience enough context to understand the request, the user's response, and current status. Explain unfamiliar technical details in plain language when they affect the outcome; omit incidental implementation mechanics.
- Distinguish backlog scope, implemented code, merged DEV changes, Staging, Production, and owner acceptance. An accepted data rollout does not prove live reminder delivery. Preserve material pending checks in the topic itself.
- Do not invent business impact, metrics, reasons, strategic decisions, adoption, or commitments. Modest leadership comes from concrete actions, not inflated claims.

## Write the spoken update

Read [the fictional style example](references/narrative-example.md) when drafting the first version. It illustrates rhythm and structure only; its content is never evidence for a reporting period.

Output the full ready-to-speak narrative in chat:

1. One short opening addressed to the requested audience, connecting the week's focus. Avoid a research preamble.
2. A bold label for every topic: **Regarding the Operations Dashboard**, **Regarding the Training Portal**, and so on. Use bold text, not numbered sections.
3. Unordered bullets under each label, written as complete, conversational sentences. Usually 2–4 bullets for a major topic and fewer for a minor one; use the evidence and speaking time to decide.
4. A brief note outside the script only for material evidence cutoff, access gaps, or unverified status. Link the evidence/cited report there on the initial delivery when useful. Do not place ticket keys, citations, evidence counts, involvement tags, or research commentary inside spoken bullets unless requested.

Aim for roughly 300–390 spoken words, then read it for cadence and a realistic 2–3 minute delivery. Do not pad thin evidence to hit a length target. A user-requested shorter or longer version overrides this target.

The title already introduces the topic: start its first bullet directly with the substance, not “Moving on,” “Regarding,” “Beyond that,” or “Finally.” Balance transitions in later bullets. Mix occasional connectors with phrases whose subjects create continuity: “The release also involved…,” “Those conversations helped define…,” “Slack reminders were the other main focus,” or “The remaining step is…”. Do not prepend a stock connector to every bullet or repeat one pattern mechanically. The bullets should sound like one person talking, not a checklist read aloud.

Do not add a forced Director ask, priority negotiation, proposed ordering of projects, closing recommendation, bench, rehearsal instruction, or fixed risk slot. Include an ask or prioritization proposal only when the user requests it. Explain an actual risk or pending acceptance naturally within its application topic.

## Revisions and delivery

Preserve every accepted correction across revisions: topic grouping, “I” ownership, bold Regarding labels, unordered narrative bullets, owner-request context, varied transitions, and removed passages. A request to improve one paragraph changes that paragraph; “final version” returns the entire revised script. Do not restore deleted priority/ask language in a later rewrite.

Reuse the current case's evidence for editorial changes. Refresh only when the user asks for current status or a material fact is stale or contradicted; do not restart intake or the weekly investigation for a wording edit.

Return the script directly even when a supporting document exists. Honor an explicitly requested save destination. A selected Page alone does not authorize editing it; if asked to save/update the narrative, use the relevant document skill and verify the saved content. This skill does not authorize messages, sharing, publishing, ticket changes, or scheduling.

Historical drafts may supply evidence when relevant, but use the current request's format and reporting window. Preserve existing report history; do not treat a draft as proof it was presented.

Before delivery, check attribution and status against the case file, confirm owner reasons are supported, keep features under their applications, and read the script aloud mentally for natural transitions and timing.
