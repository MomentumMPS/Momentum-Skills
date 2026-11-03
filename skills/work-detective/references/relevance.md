# Relevance rubric: proof of work vs. noise

The skill's reach is wide, so its filter has to be strict. An item earns a line in the evidence file only if it is proof that work moved, not that the user was present. Apply this at recording time, per item, not afterwards in bulk.

## The meeting test

Imagine the user saying the item aloud in a status meeting with their manager and peers. Keep it if (a) it describes something they did, (b) a listener who was there would nod, and (c) it would be awkward to leave out. "I shipped the pricing proposal to Marcus" passes. "I replied 'thanks' in #general" fails all three.

## Strength tiers

Record a tier with each item; it decides ordering in the report and whether the item survives when a theme is trimmed.

**Tier 1 — Outcomes.** Something exists or changed because of the user: merged PR, closed ticket, published doc, sent deliverable, decision recorded, incident resolved, meeting the user organized that produced a decision.

**Tier 2 — Progress.** A concrete, named step toward an outcome: draft shared for review, review given with substantive comments, root cause posted, estimate delivered, plan or spec written, question answered that unblocked someone, substantive contribution in a transcript.

**Tier 3 — Participation.** The user was part of real work without a visible deliverable: attended a working session, was consulted in a thread and replied with substance, was assigned something still in progress. Keep only when the intake involvement level allows it, and only when the underlying work is itself substantive.

**Noise — never recorded.** Presence, courtesy, automation, and other people's work:
- greetings, thanks, "+1", "sounds good", "will do", emoji reactions, scheduling back-and-forth
- newsletters, digests, calendar auto-replies, CI notifications, ticket bot updates, "X shared a file with you" without a follow-up by the user
- FYI/CC emails the user never replied to or acted on
- recurring meetings where no contribution by the user can be found (count them once in Routine instead)
- documents or pages the user only opened or viewed
- a colleague's message that merely mentions the user
- a conversation with an AI assistant that led nowhere identifiable (a question, no artifact, no follow-up)

## Per-source examples

**Slack.** Keep: an announcement of something done; a root-cause or design message; a substantive answer in a thread; a request that led to work; a file or link to a deliverable. Drop: standup "today I'll…" messages unless nothing else exists for that day, social channels, reactions, one-liners.

**Email.** Keep: sent emails with content (a decision, an answer, a document, an ask that someone acted on). Drop: forwards without comment, calendar accepts, replies under one line, anything in Promotions/Updates, threads the user only received.

**Calendar.** Keep: meetings the user organized; 1:1s and reviews where another source shows an outcome; working sessions on a named theme. Drop into Routine: recurring standups, all-hands, socials. Drop entirely: declined or tentative events, holds, focus-time blocks.

**Transcripts.** Keep: what the user said when it was a decision, an update, a proposal, or an answer. Drop: small talk, "can you hear me", agreement noises.

**Documents.** Keep: files the user created or substantially edited in range (dozens of edits, new sections), and comments or suggestions that changed the doc. Drop: trivial edits (typos, formatting), files only viewed, templates, auto-generated transcripts the user didn't author.

**Tickets.** Keep: created, transitioned (especially to Done), substantive comments, estimates. Drop: watched tickets, label-only changes, bot transitions.

**Code.** Keep: merged PRs, meaningful reviews, commits on named features. Drop: merge commits, dependency bumps, formatting-only changes unless that was the task.

**AI conversations.** Keep: sessions whose subject matches work found elsewhere, or that produced something (code, draft, analysis) the user then used. Drop: idle questions, tests, anything personal.

## Clustering and trimming

After collection, each theme should rest on at least one Tier 1 or Tier 2 item; otherwise fold it into Routine or drop it. Within a theme, if more than about eight items remain for a week-long range, merge near-duplicates (five messages in one thread become one line) and keep the ones that show movement. The report is judged by its weakest line, so cut toward strength.
