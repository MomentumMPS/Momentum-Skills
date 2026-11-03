# Ticket title and description

The Jira summary must use `APP-OR-PROJECT-TITLE - Description of the ticket`: the real app or project display title, followed by a space, a hyphen, a space, and the ticket description. Do not wrap either part in square brackets. Example: `Training Portal - Add a completion-date filter`.

Use these sections in this order. The four bold labels belong inside Overview. Keep **Fix:** completely blank: no proposed solution, placeholder, dash, or `TBD`. Acceptance criteria describe observable outcomes without filling in Fix indirectly with an implementation plan.

```text
Overview

What this is / Why is Necessary:
Explain why the ticket exists and why the work is needed.

Problem:
Describe the problem it resolves. Include known actual/expected behavior,
reproduction steps, and impact here when relevant; do not invent evidence.

Fix:

If we skip it:
Explain the plausible consequence of leaving the problem unresolved.

Implementation Classification
Choose exactly one: CODE SOLUTION NEEDED or NO CODE SOLUTION NEEDED.
Briefly explain why this classification applies to the requested scope.

Belongs to Improvement(s)
Include only when an identified requirement or improvement exists.
Name it and include its key/link or supplied reference.

Acceptance Criteria
- Specific, observable conditions that demonstrate the requested outcome.

Definition of Done
- Completion and verification requirements appropriate to this ticket.
```

The explanatory text above is drafting guidance, not literal content. Omit the entire **Belongs to Improvement(s)** section when there is no identified requirement; do not add `None` or infer a requirement solely because there is a parent. Use headings and bold Overview labels in ADF when supported. Plain text fallback must preserve the same structure and empty Fix. Keep Definition of Done proportional: relevant validation, review, and evidence of completion; include deployment or documentation only when the work requires it.

## Implementation classification guidance

Always include **Implementation Classification** immediately after Overview. Highlight exactly one of these labels in bold (ADF strong text for Jira or Markdown bold for chat drafts), followed by a short, ticket-specific rationale:

- **CODE SOLUTION NEEDED**: The requested outcome requires repository file changes or Git delivery work, including application code, tests, scripts, dependencies, lockfiles, CI/IaC, tracked configuration, repository documentation, or branch creation. Declarative configuration edits count even without custom application logic. Explain the required change and use this classification for mixed tickets with any required repository work.
- **NO CODE SOLUTION NEEDED**: The requested outcome can be delivered through investigation, explanation, existing functionality, or authorized setup, permissions, provisioning, and operational actions in an existing external UI/API, without repository changes or Git delivery artifacts. Identify the relevant capability or evidence. Do not require branches, worktrees, commits or PRs merely to deliver the report or record evidence.

Base the choice on known requirements and evidence; do not invent a technical design. If the distinction cannot be established, resolve the missing information before finalizing the classification rather than guessing. Keep the rationale at the scope level so agents understand the nature of the work; leave **Fix:** completely blank.
