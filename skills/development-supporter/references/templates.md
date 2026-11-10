# Output templates

Read only the needed section. Scale these templates to the actual change; a small fix needs a concise spec and PR, not empty boilerplate. They are internal/chat progress and repository-delivery artifacts, not Jira descriptions or comment templates and not automatic approval forms. Follow the main writing rules. `jira-ticket-supporter` translates relevant outcomes for Jira; do not paste these templates or review records into tickets/comments.

## Ticket brief (code checkpoint 2 / no-code N1)

```markdown
### ABC-123: Login redirect fails after session expires
Type: Bug (Jira: Bug)   Status: To Do   Priority: High   Points: 3
Assignee: unassigned   Reporter: Ana Perez   Sprint: Sprint 42
Link: https://acme.atlassian.net/browse/ABC-123
Solution: CODE SOLUTION NEEDED | NO CODE SOLUTION NEEDED
Reason and source: <required repository change or non-code outcome; user instruction / field / comment / evidence>
Requested endpoint: <investigation / proposal / local change / end-to-end delivery>

Description: <converted description, trimmed to what matters>
Acceptance criteria: <from Jira, or "missing, establish during investigation">
Repro steps: <from Jira, bugs only>
Context: parent ABC-100 (Auth revamp), relates to ABC-98
Attachments: login-error.png, session.har
Warnings: <blocked by ABC-120 (open) / already In Progress by someone else / existing branch found / none>
Missing info: <only what Jira did not answer, max 5 questions>
```

The remaining templates apply only to CODE SOLUTION NEEDED. No-code deliverables are defined in `references/no-code-solution.md`; do not generate a repository spec or PR to fill these templates.

## Spec (SDD)

```markdown
## Spec: <KEY> <ticket title>
Ticket: <link>   Type: bug | feature | ...   Environment: <chosen>

### Problem
<one paragraph: what is wrong or missing, and for whom>

### Acceptance criteria
- AC-1: Given <context>, when <action>, then <observable result>.
- AC-2: ...
Source: <Jira field / Jira description / drafted from requested behavior; flag unresolved product choices>

### Out of scope
- <items deliberately not handled>

### Approach
- <file or module>: <change and why>

### Test plan
- AC-1 -> <test file and test name, or manual steps>

### Risks and rollback
- <risk> -> <mitigation>. Rollback: revert the PR.

### Open questions
- <anything still unclear>
```

ACs must be observable and testable. "Works correctly" is not an AC. When Jira already has ACs, keep their meaning and wording, only rewrite into Given/When/Then if needed, and mark any AC you added.

## Findings table (bugs)

```markdown
### In scope
| ID | Severity | Title | Location | Expected vs Actual | Evidence |
|---|---|---|---|---|---|
| B-01 | CRITICAL | Session expiry drops return URL | src/auth/redirect.ts:42 | Expected: back to /reports. Actual: lands on /home | console log, screenshot 1 |

### Out of scope (informational, usually not fixed, candidates for future work)
| ID | Severity | Title | Location | Notes | Follow-up ticket? |
|---|---|---|---|---|---|
| *O-01* | *MEDIUM (OOS)* | *Footer links 404 on mobile* | *src/layout/Footer.tsx* | *Unrelated to auth flow* | *proposed* |
```

Below the tables, list the reproduction steps for each in-scope ID. Use gray via `<span style="color:gray">` only if the surface renders HTML.

## Feature gap table

```markdown
| Capability | Status | Location | Notes |
|---|---|---|---|
| CSV serializer | Exists | src/utils/csv.ts | Reusable as is |
| Export button | Missing | n/a | Needs design check |
| Reports API pagination | Partial | api/reports.py:88 | Max 100 rows, export needs all |
```

## Demo

```markdown
### Demo: <KEY> <ticket title>
| AC | Result | How it was shown |
|---|---|---|
| AC-1 | PASS | Steps 1-4 on /reports, screenshot 2 |
| AC-2 | PASS | Unit test reports.export.test.ts plus manual check |

Checks: <actual relevant commands/results; skipped or unavailable checks and why>
Specialist review: <not required and reason / reviewer, target, risk and verdict>
Files changed: 6 (list)
Known limitations: <if any>
Jira requirements: unchanged since last verified snapshot / material changes and resolution / not re-read, reason
```

## PR body

If the repo has a PR template, fill it and merge these sections into it.

```markdown
## Summary
<two or three sentences: what this PR does and why>

## Ticket
[<KEY>](https://<site>/browse/<KEY>): <ticket title>

## Context and problem
<the problem as understood, root cause for bugs>

## Decisions and reasoning
<the core of the PR. For each meaningful decision:>
- **Decision:** <what was chosen>
  - Options considered: <A, B>
  - Why: <reasoning>
  - Trade-off: <what was given up>

## Changes
- <file or area>: <change>

## How to test
1. <steps a reviewer can follow, environment to use>

## Evidence
<test results, screenshots, before/after>

## Out of scope and follow-ups
- <O-01: summary> -> <FOLLOW-UP-KEY or "not ticketed">

## Risks and rollback
<risks, and how to roll back>
```
