# Jira ownership and handoff

Read [Jira Ticket Supporter](../../jira-ticket-supporter/SKILL.md) for all Jira operations, including reads, searches, field discovery, comments, description edits, transitions, assignment and links. It also owns every `acli` invocation. This compatibility reference intentionally contains no command, payload or comment template.

`acli` is read-only for Development Supporter. It must never execute a Jira mutation or a write payload returned by another worker. Jira Ticket Supporter owns preparation, execution and read-back; no script, alternate client or generic delegate may bypass that ownership. If the owner is unavailable, leave sync pending.

Development Supporter supplies the key or bounded selection scope, requested endpoint, substantive requirements, verified findings, relevant checks, material limitations and existing authorization. Keep the internal code/no-code decision, reviewer names/verdicts, branch hashes, raw logs and detailed evidence in working context unless a specific detail is essential for the reader's action.

The Jira owner returns fetched context or verified mutation results and any incomplete action. Read-only/investigation-only requests stay read-only; a findings-comment request does not authorize description or status changes. Preserve existing requirements and unrelated ADF content. Do not manufacture Fix sections, code classifications or process checklists to satisfy an old template.
