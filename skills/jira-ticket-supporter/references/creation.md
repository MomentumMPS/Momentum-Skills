# New-ticket fields and delivery

Read only when creating a ticket. These defaults do not apply to a read, comment, transition, or unrelated field edit. Do not publish account IDs, field IDs, estimation arithmetic, or parent-memory records in ticket prose.

## Resolve defaults and parent memory

Read `$XDG_STATE_HOME/jira-ticket-supporter/project-memory.json` when configured, otherwise `~/.local/state/jira-ticket-supporter/project-memory.json`, for this site/project/app and ticket type. Keep this private runtime file outside the skill and repository. If absent, start with `{"version": 1, "projects": []}`. Preserve and migrate older `references/project-memory.json` to this user-state location before retiring the old installation. Do not store tokens, credentials, or full ticket descriptions in it.

| Field | Required default and resolution |
| --- | --- |
| Assignee | Use the explicitly requested assignee or current team default; otherwise resolve the intended assignee with the user. Verify the unique account identifier with acli; use `@me` only for the verified intended assignee. Never choose someone by display-name resemblance. |
| Reporter | Use an explicitly requested reporter; otherwise use the verified authenticated user creating the ticket. Resolve independently from the assignee and use the supported account identifier. |
| Labels | Find an existing label related to the actual app/project from relevant tickets. If none fits, create a meaningful lowercase hyphenated label by assigning it on the new ticket; do not create a Jira field or project. Preserve explicitly requested labels. |
| Sprint | The **current active sprint** for the applicable board. Discover boards and active sprints with acli. Use a remembered board only after validating relevance. Never reuse a cached sprint as current, choose a closed/future sprint, or create/start a sprint to satisfy this default. If none exists or multiple candidates remain ambiguous, resolve with the user before creating. |
| Story point estimate | Use the current team's agreed method, or resolve use of the suggested formula and Fibonacci scale in [estimation.md](estimation.md). Discover the project's actual estimation field ID/schema and ensure it represents points, not an hours-based estimate. |
| Parent | Reuse a previously user-confirmed, applicable parent after checking that it still exists, is suitable, and is compatible with this child type. If no such record exists, search plausible parents with acli and present the candidate key, title, and reason to the user for confirmation **before using it**. An explicit parent supplied by the user counts as confirmation. If none fits, ask how to proceed; do not invent a parent or create one automatically. |

For active sprint discovery, check current help; installed command shapes include:

```sh
acli jira board search --project 'PROJECT' --json
acli jira board list-sprints --id 'BOARD_ID' --state active --json
```

After user confirmation **and verification of parent suitability and hierarchy compatibility**, persist an entry in the private user-state `project-memory.json` location above containing `site`, `project_key`, `app_title`, `child_type`, `parent_key`, `parent_summary`, `confirmed_at`, and `confirmation_source` (a brief description of the user's confirmation). Scope it precisely enough that different apps or child types in the same Jira project do not inherit the wrong parent. Optional verified `board_id` and intended account ID can be stored with the same scope. Preserve unrelated entries and write valid JSON atomically. Do not store an unconfirmed or incompatible candidate as approved. If multiple records apply, resolve ambiguity. Reconfirm only when scope changes, the parent becomes invalid, or the user requests another parent. If memory cannot be saved, report that persistence failed and do not imply it was remembered.


## Verify field support before writing

Inspect `acli jira workitem create --help` and `--generate-json` in a temporary directory. Use the installed schema, not Jira REST payload assumptions. The observed create JSON supports `projectKey`, `type`, `summary`, ADF `description`, `assignee`, `reporter`, `labels`, `parentIssueId`, and `additionalAttributes` for custom fields. Sample `customfield_10000` IDs are illustrative: never copy them as real sprint or point fields.

Resolve sprint and point field IDs/types using acli-accessible schema or verified field mappings and relevant tickets. Do not infer a field's meaning from a numeric value alone. If the installed acli cannot expose enough metadata, request verified configuration from the user; do not fetch it through another Jira client. Verify whether parent support applies to the selected hierarchy: the observed JSON example describes `parentIssueId` as subtask-only, while `--parent` exists as a flag. Do not assume arbitrary parent relationships or combine `--from-json` with flags unless current help/documentation supports it.

Set reporter, sprint, estimate, and the other defaults in the create payload when supported. A follow-up acli edit of the newly created ticket is within scope only if needed to finish these fields and a supported path has been established before creation. The observed edit JSON does not advertise custom attributes; do not assume it can repair sprint/points. If any required default cannot be resolved or written with acli, stop before creation, explain the concrete limitation, and ask for the missing value or an explicit exception. Never silently omit a requirement or switch tools.
