---
name: jira-ticket-supporter
description: Draft and create Jira tickets with acli using reusable title and description templates, verified assignment, sprint, estimation, and parent context. Use for filing Jira bugs, stories, tasks, epics, or subtasks from requirements or findings; does not implement tickets or manage unrelated existing work.
---

# Jira Ticket Supporter

Create actionable tickets using the templates and resolution rules below. Honor the current user or team's explicit format and defaults. For draft-only requests, return a draft without Jira writes. Creating or testing this skill does not authorize live sample tickets. Explicit instructions for the current request override defaults; otherwise follow every requirement and disclose blockers rather than silently omitting fields.

## 1. Establish context using acli

**Use `acli` for every Jira operation**, including authentication, reads, searches, creation, and any necessary follow-up edits. Do not use Jira connectors, direct HTTP/API calls, browser operations, or alternative clients as a fallback.

Follow the current host's sandbox and approval rules. If authentication fails because the sandbox cannot access the CLI session or network, use an authorized execution context before requesting login. Otherwise request the normal interactive login flow, never credentials in chat.

Resolve the Jira site, project key, app/project display title, ticket type, and scope from trusted current context. Ask only for unresolved information; do not borrow defaults from unrelated chats. Inspect installed CLI help before using unfamiliar commands or payload fields. Search for likely duplicates before filing findings or a batch; a search failure does not establish absence. Resolve a likely duplicate with the user before creating another or editing it.

## 2. Resolve defaults and parent memory

Read `$XDG_STATE_HOME/jira-ticket-supporter/project-memory.json` when that user-state directory is configured, otherwise `~/.local/state/jira-ticket-supporter/project-memory.json`, for this site/project/app and ticket type. Keep this private runtime file outside the skill and repository. If it does not exist, start with `{"version": 1, "projects": []}`. Do not store tokens, credentials, or full ticket descriptions in it. When upgrading an older installation, preserve its `references/project-memory.json` outside the repository and migrate it to this user-state location before retiring the old installation.

| Field | Required default and resolution |
| --- | --- |
| Assignee | Use the person explicitly requested by the user or established by the team's current defaults. If none is specified, ask whether to assign to the verified authenticated user or another person. Resolve the unique account ID/email with acli; use `@me` only for the verified intended assignee. Never choose someone by display-name resemblance. |
| Reporter | Use an explicitly requested reporter; otherwise use the verified authenticated user creating the ticket. Resolve independently from the assignee and use the account identifier supported by the CLI payload. |
| Labels | Find an existing label related to the actual app/project from relevant tickets. If none fits, create a meaningful lowercase hyphenated label by assigning it on the new ticket; do not create a Jira field or project. Preserve explicitly requested labels. |
| Sprint | The **current active sprint** for the applicable board. Discover boards and active sprints with acli. Use a remembered board only after validating relevance. Never reuse a cached sprint as current, choose a closed/future sprint, or create/start a sprint to satisfy this default. If none exists or multiple candidates remain ambiguous, resolve with the user before creating. |
| Story point estimate | Use the current team's estimation method, or resolve use of the suggested formula and Fibonacci scale in [references/estimation.md](references/estimation.md). Discover the project's actual estimation field ID/schema and ensure it represents points, not an hours-based estimate. |
| Parent | Reuse a previously user-confirmed, applicable parent after checking that it still exists, is suitable, and is compatible with this child type. If no such record exists, search plausible parents with acli and present the candidate key, title, and reason to the user for confirmation **before using it**. An explicit parent supplied by the user counts as confirmation. If none fits, ask how to proceed; do not invent a parent or create one automatically. |

For active sprint discovery, check current help; installed command shapes include:

```sh
acli jira board search --project 'PROJECT' --json
acli jira board list-sprints --id 'BOARD_ID' --state active --json
```

After user confirmation **and verification of parent suitability and hierarchy compatibility**, persist an entry in the private `project-memory.json` location above (create its parent directory if needed) containing `site`, `project_key`, `app_title`, `child_type`, `parent_key`, `parent_summary`, `confirmed_at`, and `confirmation_source` (a brief description of the user's confirmation). Scope it precisely enough that different apps or child types in the same Jira project do not inherit the wrong parent. Optional verified `board_id` and the intended account ID can be stored with the same scope. Preserve unrelated entries and write valid JSON atomically. Do not store an unconfirmed or incompatible candidate as approved. If multiple records apply, resolve ambiguity. Reconfirm only when scope changes, the parent becomes invalid, or the user requests another parent. If memory cannot be saved, report that persistence failed and do not imply it was remembered.

## 3. Draft the required content and estimate

Read [references/ticket-template.md](references/ticket-template.md) and follow its title syntax, section order, and conditional requirement section exactly. **Fix is always blank.** Separate evidence from assumptions. Preserve the requested scope; do not split work into extra tickets without authorization. Include the mandatory Implementation Classification with exactly one highlighted code-solution label and a concise rationale and its source, following the template guidance. Classify before estimating; align acceptance criteria and Definition of Done with the selected scope. Ticket creation does not authorize executing either solution path.

Read the estimation reference and apply the agreed method. When using its suggested formula, calculate all five inputs, the net result, and the Fibonacci selection. Prepare a concise pre-creation summary with title, target project/type, parent, assignee/reporter, labels, active sprint, solution classification with reason/source, points, and the estimation rationale. Estimate only the selected scope: no implementation or PR effort for no-code or branch-setup-only tickets, and no Git delivery effort for no-code tickets. If parent approval or another decision is needed, prepare the complete draft and resolve that decision before writing. A request to create tickets already authorizes creation and these defaults; do not request a redundant final confirmation.

## 4. Verify field support before writing

Inspect `acli jira workitem create --help` and `--generate-json` in a temporary directory. Use the installed schema, not Jira REST payload assumptions. The observed create JSON supports `projectKey`, `type`, `summary`, ADF `description`, `assignee`, `reporter`, `labels`, `parentIssueId`, and `additionalAttributes` for custom fields. Sample `customfield_10000` IDs are illustrative: never copy them as real sprint or point fields.

Resolve sprint and point field IDs/types using acli-accessible schema or verified field mappings and relevant tickets. Do not infer a field's meaning from a numeric value alone. If the installed acli cannot expose enough metadata, request verified configuration from the user; do not fetch it through another Jira client. Verify whether parent support applies to the selected hierarchy: the observed JSON example describes `parentIssueId` as subtask-only, while `--parent` exists as a flag. Do not assume arbitrary parent relationships or combine `--from-json` with flags unless current help/documentation supports it.

Set reporter, sprint, estimate, and the other defaults in the create payload when supported. A follow-up acli edit of the newly created ticket is within scope only if needed to finish these fields and a supported path has been established before creation. The observed edit JSON does not advertise custom attributes; do not assume it can repair sprint/points. If any required default cannot be resolved or written with acli, stop before creation, explain the concrete limitation, and ask for the missing value or an explicit exception. Never silently omit a requirement or switch tools.

## 5. Create, verify, and report

Write multiline descriptions or full JSON payloads as temporary UTF-8 files using safe file tools or serializers. Use ADF for headings and bold labels with `--from-json`; preserve the empty Fix. Plain text via `--description-file` is acceptable if it preserves the template. Never interpolate ticket text as executable shell code.

Use the verified command/payload and structured output, for example `acli jira workitem create --from-json '/absolute/path/to/ticket.json' --json`. Capture the returned key immediately. Verify with `acli jira workitem view KEY-123 --json`, requesting all relevant fields as necessary. Check exact summary, description structure and blank Fix, exactly one highlighted classification with its rationale/source and consistent acceptance criteria/Definition of Done, assignee, reporter, labels, parent, active sprint ID, and numeric point value. Complete only supported follow-up field writes on that known key, then verify them.

On a timeout or ambiguous create response, search and inspect matching tickets before any retry. Retry only after establishing no ticket was created; otherwise stop and report uncertainty. On explicit validation rejection, correct verified values within scope; stop after repeated rejection instead of guessing payloads. If creation succeeded but fields or verification failed, report the known key and incomplete requirements; do not create a replacement. For batches, preserve completed keys and stop further creation on ambiguous outcomes.

Return created keys, summaries, verified browse links, and the actual saved defaults, including sprint and points. Disclose any explicitly approved exceptions, failures, or verification limits. Do not report success merely because the ticket exists. Do not transition work, comment, add issue links, implement code, or send messages unless separately requested.
