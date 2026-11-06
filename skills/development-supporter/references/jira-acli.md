# Jira via Atlassian CLI (acli): reference

Read this file when SKILL.md tells you to. Sections:
1. Preflight
2. Finding the ticket
3. Fetching everything about the ticket
4. Extracting fields
5. Project config file (status mapping and field IDs)
6. Write commands
7. Comment templates
8. Errors

Use `--json` on data read commands when supported; auth/help/version commands may use text output. If a flag below is rejected by the installed version, run the command with `--help` and adapt. Do not guess flags on write commands.

## 1. Preflight

```bash
acli --version
acli jira auth status
```

- `acli` missing: tell the user to install it (https://developer.atlassian.com/cloud/acli/guides/install-acli/) and stop the Jira part. The rest of the workflow can continue with manually provided ticket data.
- Follow the current host's sandbox and approval rules. If sandbox restrictions prevent access to the authenticated CLI session or network, retry in an authorized execution context before diagnosing authentication. Tool permission does not authorize extra Jira writes.
- Not authenticated after that check: ask the user to run `acli jira auth login --web` themselves. Never ask for, accept, print or store an API token in chat or in files.
- Note the site from `auth status` (for example `acme.atlassian.net`). Ticket links are `https://<site>/browse/<KEY>`.

## 2. Finding the ticket

**Key given directly** (`ABC-123`, any case): uppercase it.

**URL given:** extract the key from `/browse/ABC-123`, `selectedIssue=ABC-123`, or `/issues/ABC-123`.

**Nothing given:** list the user's open work and let them pick:

```bash
acli jira workitem search \
  --jql "assignee = currentUser() AND sprint in openSprints() AND statusCategory != Done ORDER BY priority DESC, updated DESC" \
  --fields "key,summary,status,priority,issuetype" --limit 10 --json
```

If that errors (Kanban project, no sprints), retry without `AND sprint in openSprints()`.

**Duplicate work check** when an existing repository is available (read only; do not fetch or create a checkout for this):

```bash
git branch -a | grep -i "<key>"
gh pr list --state all --search "<KEY>" 2>/dev/null
```

## 3. Fetching everything about the ticket

```bash
KEY=ABC-123
acli jira workitem view "$KEY" --fields "*all" --json > /tmp/$KEY.json
acli jira workitem comment list --key "$KEY" --json > /tmp/$KEY-comments.json
acli jira workitem link list --key "$KEY" --json > /tmp/$KEY-links.json
acli jira workitem attachment list --key "$KEY" --json > /tmp/$KEY-attachments.json
```

Then, only when relevant:
- **Parent or epic** (`fields.parent.key`): `acli jira workitem view <PARENT> --fields "summary,description,status" --json` for context. Read only the summary and description.
- **Linked items** of type blocks / is blocked by / relates / duplicates / clones: view summary and status of each. An unresolved "is blocked by" link is a warning in the brief; assess whether it actually blocks the requested work.
- **Subtasks** (`fields.subtasks`): list them with status.
- **Confluence links** in the description: if a Confluence command or Atlassian MCP is available, read them. Otherwise list them and ask whether they matter.
- **Attachments:** list names and types. Screenshots and recordings attached to bugs are often essential for reproduction. If they cannot be downloaded with the tools available, give the user the list and ask them to share the relevant ones.

Keep the JSON files in `/tmp`, never in the repo.

## 4. Extracting fields

| Brief item | Where it lives |
|---|---|
| Key, summary | `.key`, `.fields.summary` |
| Type | `.fields.issuetype.name` |
| Status | `.fields.status.name` and `.fields.status.statusCategory.key` (`new`, `indeterminate`, `done`) |
| Priority | `.fields.priority.name` |
| Assignee, reporter | `.fields.assignee.displayName`, `.fields.reporter.displayName` |
| Labels, components, fix versions | `.fields.labels`, `.fields.components[].name`, `.fields.fixVersions[].name` |
| Description | `.fields.description` (ADF, convert with the script) |
| Acceptance criteria | custom field from config, else an "Acceptance criteria" / "AC" / "Criterios de aceptacion" / "Definition of done" section in the description |
| Capacity | story points custom field from config, else `.fields.timetracking.originalEstimate` |
| Sprint | sprint custom field from config |
| Last update | `.fields.updated` (save it, used to detect changes later) |

Convert ADF fields to readable text with the bundled script:

```bash
python3 scripts/adf_to_md.py --field description < /tmp/$KEY.json
python3 scripts/adf_to_md.py --field customfield_10045 < /tmp/$KEY.json
```

Simple values with jq:

```bash
jq -r '.fields.summary, .fields.issuetype.name, .fields.status.name' /tmp/$KEY.json
```

### Type mapping

These types guide investigation only. They do not select CODE SOLUTION NEEDED; apply solution routing in SKILL.md first.

| Jira issue type | Skill path |
|---|---|
| Bug, Defect, Incident | Bug |
| Story, Feature, New Feature, Improvement, Enhancement | Feature |
| Task | Infer from description, state the inference in the brief |
| Technical Debt, Refactor | Refactor |
| Spike, Research | Spike |
| Sub-task | Use the parent's type unless the sub-task itself is clearly different |
| Epic | Not workable as one ticket. List its children and ask which one |

If open sub-tasks make the requested scope ambiguous, ask which scope to take. Reuse an explicit whole-ticket/sub-task choice.

## 5. Project config file

Status names, story point fields and AC fields differ per Jira project. During intake and on the no-code path, read any existing config and keep discoveries in conversation or `/tmp`; do not create repository files or edit git metadata. Only during authorized file implementation after routing and recon, optionally store verified config in `.codex/jira.json`, kept out of git with the repo-local exclude file (this does not modify `.gitignore`):

```bash
mkdir -p .codex
TASK_EXCLUDE=$(git rev-parse --git-path info/exclude)
grep -qx ".codex/" "$TASK_EXCLUDE" || echo ".codex/" >> "$TASK_EXCLUDE"
```

```json
{
  "project": "ABC",
  "statuses": {
    "start": "In Progress",
    "review": "In Review",
    "blocked": "Blocked"
  },
  "fields": {
    "story_points": "customfield_10016",
    "acceptance_criteria": "customfield_10045",
    "sprint": "customfield_10020"
  },
  "branch_includes_key": true
}
```

Discovery:
- **Statuses:** collect the distinct statuses used recently:
  ```bash
  acli jira workitem search --jql "project = ABC AND updated >= -60d" --fields "status" --limit 200 --json \
    | jq -r '.. | .status? | .name? // empty' | sort -u
  ```
  Propose the mapping for `start`, `review` and `blocked` (blocked is optional, use null if the workflow has none).
- **Custom fields:** values in `/tmp/$KEY.json` can suggest candidates, but cannot establish field identity. Verify field names/IDs from supported metadata, existing project configuration or user confirmation before using a mapping, especially for writes. Do not mistake a small number for confirmed story points or rich text for confirmed ACs.
- Reuse verified mappings; no separate config approval is needed. Ask only for unresolved mappings needed for a specific action. On no-code/branch-setup paths, keep mappings in conversation or temporary files. Do not create a config gate or change project instructions just to persist discoveries.

## 6. Write commands

Hard rules for every write:
- Target one existing ticket per mutation using the supported single-item selector, normally `--key <KEY>`. Creation and linking use their documented single-item arguments below. Never use JQL, filters, key lists or bulk writes. Inspect installed help/schema rather than guessing a write flag.
- Only the current ticket may be written, plus follow-up tickets the user approved by name.
- Never use `delete`, `archive`, `unarchive`, `clone`, `create-bulk`, or project, sprint, board, filter or admin write commands.
- Add `--yes` only to single-key commands, and only to skip the interactive prompt of an action already authorized under SKILL.md's authorization contract.
- Write bodies to a temp file and pass the file, to avoid shell escaping problems.

```bash
# Assign to yourself (only if unassigned, or the user approved reassignment)
acli jira workitem assign --key "$KEY" --assignee "@me" --yes

# Transition (name from config)
acli jira workitem transition --key "$KEY" --status "In Progress" --yes

# Comment (plain text, ASCII)
acli jira workitem comment create --key "$KEY" --body-file /tmp/$KEY-comment.txt

# Follow-up ticket: generate the JSON shape, fill it, create
acli jira workitem create --generate-json > /tmp/followup.json
acli jira workitem create --from-json /tmp/followup.json

# Link the follow-up to the current ticket ("Relates" has no direction issues)
acli jira workitem link type
acli jira workitem link create --out "$KEY" --in "<NEW-KEY>" --type "Relates" --yes
```

After every write, read the resource that proves that specific change, not just command success:

- Assignment/transition: read current assignee/status.
- Comment: read the saved comment by returned ID or list comments and match its content; status/assignee fields cannot verify a comment.
- Description/AC edit: read the affected field and confirm intended content plus preservation of unrelated content.
- Follow-up creation/link: read the new ticket and the actual link endpoints/type.

Refresh the ticket snapshot after verified own writes. On an ambiguous timeout, inspect current state before retrying a mutation; avoid duplicate comments, tickets or links. Report unverifiable writes as pending, not successful.

If a transition is rejected (not allowed from the current status, or the workflow requires a field such as a resolution), report the error and the current status to the user. Do not chain intermediate transitions on your own.

### Verified solution in Fix (implementation delivery / Git result / no-code N2)

For bugs and features, populate the existing **Fix:** label inside **Overview**, between **Problem:** and **If we skip it:**. This follows the jira-ticket-supporter ticket template: Fix stays blank at creation; development-supporter fills it with the verified solution during authorized end-to-end resolution. Do not claim personal user acceptance unless it occurred. A spec, PR or resolution comment does not substitute for this description update. Fix is not Jira's Fix versions field.

- State what changed or what evidence explains the resolution, and why it addresses the ticket. Include verification evidence and limitations. For no-code resolutions, start with `NO CODE SOLUTION NEEDED`, explain why repository changes are unnecessary, and record only actual actions or verified existing behavior. A proposal or inability to reproduce is not an accepted solution. Add a PR link only on the code path when available; never create one for this field.
- Show the exact Fix text and description diff before writing. Updating only this section with the verified solution is routine end-to-end sync under the main contract; investigation-only or findings-publication requests do not imply this edit. Changes to requirements or other description sections need specific authorization. Do not request routine approval or use Open All The Gates to expand scope.
- Re-fetch the current description before editing. Preserve its ADF structure, other sections, formatting, links and existing content outside Fix. Update the existing Fix content instead of appending duplicate labels. If Fix is absent, insert the label in the matching Overview position; for a legacy description without that structure, append a clearly labeled Fix section without rewriting the ticket. Show unexpected or conflicting changes to the user before overwriting them.
- Inspect `acli jira workitem edit --help` and any supported JSON schema before preparing the single-ticket description edit in a temporary file. Use only the installed CLI's supported flags and payload. Do not convert the entire description through the lossy ADF-to-Markdown reader. If the CLI cannot preserve the description, report the blocker rather than replacing it with a comment or claiming completion.
- Re-read the description after the write and confirm the accepted solution is in Fix and the other content is preserved. If Jira is unavailable, retain the proposed text and report the update as pending.

## 7. Comment templates

Plain text, no markdown tables, no emojis, no @mentions unless the user asked for one. Keep each comment short and evidence-based. Code templates below apply only on the code path; no-code comment content is defined in `references/no-code-solution.md`.

**Start** (authorized implementation setup):
```
Work started.
Branch: codex/ABC-123-login-redirect-fails-after-session-expires
Environment for reproduction: DEV
```

**Implementation plan** (when a useful plan comment is in scope):
```
Implementation plan.
Root cause: <one sentence, bugs only>
Acceptance criteria:
- AC-1: Given ..., when ..., then ...
- AC-2: ...
Out of scope: <short list or "none">
```

**Blocked or needs info** (only within authorized Jira communication scope):
```
Could not reproduce with the information available.
Tried: <3 short attempts>
Needed: <exact question for the reporter>
```

**PR opened** (after a real PR is created and verified):
```
Pull request ready for review: <PR URL>
Summary: <one or two sentences>
Follow-ups created: ABC-130, ABC-131 (or "none")
```

## 8. Errors

| Error | Action |
|---|---|
| `command not found: acli` | Section 1. Continue without Jira automation, ask for ticket data manually |
| Unauthorized / 401 | If sandbox restrictions may have affected authentication, retry in an authorized execution context first; only if still unauthenticated ask for `acli jira auth login --web` |
| Ticket not found / 404 | Check the key and site (`auth status`), the user may lack access. Ask |
| Forbidden on a write / 403 | Report it. Do not retry with other commands |
| Transition not available | Section 6. Report and ask |
| Unknown flag | Run `--help` for that command, adapt, never guess on writes |
| Rate limited / 429 | Wait 30 seconds, retry once, then report |
