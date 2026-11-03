# CODE SOLUTION NEEDED

Read this workflow only after the solution routing in SKILL.md selects CODE SOLUTION NEEDED. All paths in this reference are relative to the skill root. Shared approval, safety, writing and completion rules still apply.

## Requested branch setup (before Phase 1)

Use this bounded procedure only when creating named Git branches is itself a requested outcome or an explicitly requested prerequisite for file changes. It covers creation of missing refs at existing commits, not merging, moving/deleting existing refs, or deployment. An active NO CODE SOLUTION NEEDED restriction still requires the user's explicit scope change before entry.

1. Inspect the target repository/remote and requested source and destination refs without changing the checkout. Resolve each source to an existing commit SHA and check each destination. Do not guess a missing source, target or remote. If a destination already has the intended SHA, verify and report it as already satisfied; if it differs, report the conflict without modifying it. DEV does not need to exist when creating DEV is the requested outcome. A dirty checkout is preserved and does not block remote ref inspection or creation.
2. `GATE Git setup`: show the exact repository/remote, source ref and resolved SHA, each destination ref and current state, and proposed Jira updates. Apply the shared authorization rule. Check relevant repository automation for branch-create/push triggers before writing; if creation would deploy or cause other out-of-scope effects, obtain the required scoped authorization or report the blocker. This procedure supplies no deployment authorization.
3. Create only the authorized missing refs at the approved SHAs, using a create-only operation that fails if a destination now exists. Do not use an ordinary push that could advance a concurrently created branch. On a race or ambiguous response, re-read the remote before any retry; matching refs are satisfied, differing refs are conflicts. Verify each result against the approved SHA and report partial success honestly. Never overwrite, fast-forward, force-update, delete, switch branches, create worktrees, stage files or create commits as part of this procedure.
4. `GATE Git result`: present the requested-versus-actual refs and SHAs, acceptance evidence, and exact proposed Jira comment and any necessary description/status edits. Apply the shared authorization rule, preserve description content, and verify approved writes using `references/jira-acli.md`, section 6. Record accepted bug/feature resolutions in Fix when applicable, describing branch setup without a no-code label or invented PR link. Retain status unless a transition is authorized; do not automatically mark Done.

If branch setup is the entire ticket, completion means the requested refs are verified, the result is accepted under the shared gate rule, approved Jira sync is verified, and shared cleanup is complete. **Stop here.** Phases 1-10 and their completion checklist do not apply: no development branch, application setup, implementation spec, tests/build, commits, audit cherry-picks or PR are required merely to deliver branch setup. Failed or unverified operations remain incomplete; do not undo successful ref creation as automatic rollback.

For mixed tickets, complete only the explicitly requested setup, then enter Phase 1 for the required file changes. The normal DEV base, spec, validation and PR requirements still apply to that implementation. Never create DEV or fall back to another base for an ordinary code ticket that did not request branch setup.

## File-implementation workflow map

| Phase | Name | Gate | Jira writes on approval |
|---|---|---|---|
| 1 | Repo recon and base fetch | none | none |
| 2 | Brief, branch, environment | GATE 2 | assign, In Progress, start comment |
| 3 | Start the app | none | none |
| 4A / 4B | Bug investigation / Feature gap analysis + spec | GATE 3 | spec comment, optional AC update, optional follow-ups |
| 5A / 5B | Fix / Implement | none | none |
| 6 | Verify (includes Jira change check) | none | none |
| 7 | Demo | GATE 4 | none |
| 8 | Commits | none | none |
| 9 | Audit analysis and optional cherry-picks | GATE 5 | none |
| 10 | Push and pull request | GATE 6 | In Review, PR comment, accepted solution in Fix, approved follow-ups |

---

## Phase 1: Repo recon and base fetch (no gate)

1. Read, if present: `AGENTS.md`, `README*`, `CONTRIBUTING*`, `package.json` / `pyproject.toml` / `Makefile` / `docker-compose*`, `.env.example` and other `.env.*` names (names only, never print values), CI config, `.github/pull_request_template.md`, commitlint or husky config.
2. Identify: package manager (from the lockfile), dev, test, lint, typecheck and build commands, environment modes, default branch, whether the repo keeps specs (`specs/`, `docs/specs/`).
3. `git status`. If dirty, stop and ask: stash, commit, or abort. Never discard someone else's changes.
4. `git fetch origin` and verify that `origin/DEV` exists. Always use the latest remote `DEV` branch (case-sensitive) as the base for new work branches. Do not choose the repo default branch or a Jira fix-version release branch as the base. If `origin/DEV` is missing or the fetch fails, stop branch creation and report the problem; never silently fall back to `main`, `master`, or `develop`.

## Phase 2: Brief, branch and environment (GATE 2)

### Branch naming

Format: `codex/<KEY>-<title-slug>`, for example `codex/ABC-123-login-redirect-fails-after-session-expires`.

- The key stays uppercase. Jira links branches, commits and PRs to a ticket by finding the key in their names, and uppercase is the form it always recognizes.
- The slug follows the Jira summary. Rules in order: transliterate to ASCII (`configuración` -> `configuracion`), lowercase, replace each run of characters outside `a-z0-9` with one `-`, trim dashes, cap at 60 characters at a word boundary. Strip a leading `[KEY]` or `KEY:` from the summary first so the key is not repeated.
- If `.codex/jira.json` sets `branch_includes_key: false`, use `codex/<title-slug>`.
- If the branch already exists locally or on the remote, ask: reuse it or create one with `-v2`.

### Environment options

List every option detected and its source (script name or env file), typically LOCAL / API, DEV, STG, PRODUCTION. Mark the risk:
- **LOCAL, DEV:** safe for any action.
- **STG, PRODUCTION:** shared or real data. Any write (create, edit, delete, payment, email, notification) affects real records or users.

If the ticket says where the bug was seen, recommend reproducing in the safest environment that shows it. If the user picks STG or PRODUCTION, reproduction becomes read only, with every write action confirmed one by one.

### Gate 2 message

One message containing:
1. The ticket brief (`references/templates.md`, Ticket brief), including solution classification, evidence, warnings and at most 5 questions for real gaps. If Jira answered everything, say so and ask nothing extra.
2. Project config proposal, only the first time for this Jira project.
3. Repo summary in two to five lines.
4. Proposed branch and base branch (`DEV`).
5. Environment options with risk labels.
6. The Jira updates that will happen on approval: assign to you (only if unassigned), move to the configured start status, post the start comment.

`GATE 2`: apply the Gate approval contract in SKILL.md. If any setup decision or proposed write is uncovered, present it and end the turn with the gate WAITING. Once authorized, create the branch, then apply the Jira updates (reference section 6) and confirm each one by re-reading the ticket.

```bash
git fetch origin
git switch -c codex/<KEY>-<slug> origin/DEV
```

## Phase 3: Start the app (no gate)

1. **Dependencies:** install only if missing or out of date, with the lockfile-respecting command (`npm ci`, `pnpm install --frozen-lockfile`, `yarn install --immutable`, `pip install -r ...`). Ask first if an install would modify the lockfile.
2. **Port:** use a fresh free port, checked first (`lsof -i :<port>`). Never kill a process you did not start. Read the real URL from the server output.
3. **Run in background** with logs in `/tmp/<KEY>-dev.log`, never inside the repo.
4. **Wait for ready:** poll until it responds or 120 seconds pass. On failure show the last 40 log lines, diagnose, retry at most twice, then report.
5. **Browser tool**, in this order: built-in web view, Playwright or Chrome DevTools MCP, headless Playwright script with screenshots, or ask the user to check manually and share screenshots. Say which one you use.
6. **Auth:** ask for test credentials if login is needed. Never hardcode, log or commit them, and never use someone's personal production account. Credentials pasted in Jira are not to be copied anywhere.

---

## IF the ticket is a BUG

### Phase 4A: Investigate, reproduce, spec (GATE 3)

1. **Start from Jira's repro steps,** attachments and comments. Locate the affected code: routes, components, error messages, endpoints. Use `git log -S "<snippet>"` and `git blame` to find recent changes in the area.
2. **Reproduce in the browser step by step.** Record action, expected, actual for each step. Collect evidence: console errors, failing network requests (method, endpoint, status, payload with secrets masked), screenshots.
3. **Cannot reproduce** after 3 distinct attempts (different data, role, viewport, browser state, environment): stop, report what you tried, and offer to post the "needs info" comment to Jira (and move to the blocked status if configured). Both require approval. Do not fix an unreproduced bug on a guess unless the user says so.
4. **Root cause:** the cause, not the symptom, in two to four sentences with `file:line`.
5. **Log everything else you notice** and classify it with the rules below.
6. **Draft the spec** (`references/templates.md`, Spec). Reuse Jira's ACs. If Jira has none, draft them and mark them as drafted.

**Severity**
- **CRITICAL:** blocks the main flow, crash, data loss or corruption, security exposure, or wrong result with no workaround.
- **MEDIUM:** works but degraded: edge case failures, broken on one viewport or browser, workaround exists, noticeable UX defect.
- **SMALL:** cosmetic, copy, minor alignment, console warnings with no user impact.

**Scope test:** "Would this make the ticket's acceptance criteria fail, or the flow described in the ticket wrong?" Yes: in scope. No: out of scope (OOS). Unsure: mark in scope with `?` and ask. Security issues are always flagged prominently, even when OOS.

**Findings table:** `references/templates.md`, Findings table. IDs `B-xx` in scope, `O-xx` OOS, ordered by severity, OOS in a separate muted table.

Before presenting `GATE 3`, complete the separate proposal review and automatic correction loop required by SKILL.md. Include the current spec revision and review verdict in the gate package.

`GATE 3` message: root cause, findings tables, spec, and the Jira actions on approval:
- Post the spec comment (always proposed).
- Write drafted ACs into the Jira AC field or description (only if Jira had none, opt-in).
- Create follow-up tickets for chosen OOS items, linked as "Relates" (opt-in, list each one with its summary).

Recommend fixing all in-scope CRITICAL and MEDIUM items and ask which IDs to fix. OOS items are fixed only if the user names them, in separate commits.

### Phase 5A: Fix (progress updates, no gate)

1. One finding at a time, in severity order.
2. **Test first where test infra exists:** a regression test that fails on current code, then the fix until it passes. Without test infra, write down manual verification steps.
3. **Minimal diff:** no drive-by refactors, renames or formatting of untouched code.
4. Progress update after each fix: ID, what changed, test added.
5. If the root cause proves wrong, stop and update the user before continuing.

Then go to Phase 6.

---

## IF the ticket is a FEATURE

### Phase 4B: Gap analysis and plan (GATE 3)

1. **Inventory what exists** (components, endpoints, models, feature flags, tests) against the Jira ACs: `references/templates.md`, Feature gap table.
2. **Implementation plan** inside the spec: files to create or modify, API or data contract changes, migrations, feature flag, tests per AC, risks, explicit out-of-scope items.
3. **Capacity check:** compare against the story points or original estimate from Jira. If the plan clearly exceeds it, say so and propose a smaller first slice, with the rest as follow-up tickets.

Before presenting `GATE 3`, complete the separate proposal review and automatic correction loop required by SKILL.md. Include the current spec revision and review verdict in the gate package.

`GATE 3`: approval of inventory and plan, plus the same Jira actions as the bug path (spec comment, optional AC write-back, optional follow-ups). If the user rejects the inventory, redo step 1. If they reject the plan, redo step 2.

### Phase 5B: Implement (progress updates, no gate)

1. Small vertical slices, each mapped to one or more ACs, tests written alongside.
2. Follow existing codebase patterns. Reuse components before creating new ones.
3. Do not add or upgrade dependencies without asking.
4. Progress update after each slice: AC, change, tests.
5. If the plan proves wrong mid-way (unexpected dependency, contract change, missing API), stop and re-confirm.

Then go to Phase 6.

---

## Other ticket types

- **Chore, docs:** Feature path, scaled down, only when a repository change is actually required.
- **Refactor:** behavior must not change. Run the full test suite before and after, say so in the PR.
- **Spike:** normally use the no-code workflow for a findings report. Stay here only for an explicitly requested repository deliverable, such as a committed prototype.

## The spec (SDD)

Template in `references/templates.md`. Draft the spec in the conversation or a temporary file outside the repository for Gate 3. After Gate 3 approval, if the repo keeps specs (`specs/`, `docs/specs/`), save it as `<KEY>-<slug>.md`; commit it with `docs:` in Phase 8 after Gate 4 approval. Otherwise it lives in the conversation, the approved Jira spec comment, and the PR description. ACs must be observable and testable.

---

## Phase 6: Verify (no gate, required before demo)

1. Run the project's checks with the exact recon commands: lint, typecheck, unit tests, build, and e2e if relevant.
2. If a check fails, check whether it also fails on the base branch (`git worktree add /tmp/base origin/DEV`) before assuming you caused it. Report pre-existing failures separately.
3. Re-run the reproduction steps (bug) or AC scenarios (feature) in the browser.
4. Regression sweep: flows next to the touched code, console clean of new errors.
5. Self-review the complete ticket change against the PR destination, including staged, unstaged and relevant untracked files: debug logs, commented-out code, stray TODOs, secrets, unrelated changes, non-ASCII characters in new prose. `git diff origin/DEV...HEAD` alone omits uncommitted implementation. This hygiene check does not replace the separate Ponytail result review.
6. **Jira change check:** re-read the ticket and compare `fields.updated` with the saved value. If the description, ACs or new comments changed the requirements, stop and show the difference before the demo.

## Phase 7: Demo (GATE 4)

Complete the separate Ponytail implementation review and authorized correction loop required by SKILL.md before presenting Gate 4 as ready. Show its report in chat, including the reviewed revision, evidence, findings and verdict; a report link alone is insufficient.

Walk through every AC live in the browser and report with `references/templates.md`, Demo. Include the proposed `Fix:` text describing the implemented solution and why it resolves the bug or delivers the feature, with relevant verification evidence. Once Gate 4 is approved, this is the accepted solution to record in Jira at Gate 6; do not fill Fix with an unimplemented proposal.

`GATE 4`: approve, or describe what is wrong. Classify feedback:
- **Implementation defect** -> Phase 5A or 5B.
- **Spec misunderstanding** -> Phase 4A or 4B, correct the spec, re-approve. Update the Jira spec comment with approval.
- **New requirement** -> scope change. Ask: add it to this ticket (update spec and ACs) or create a follow-up ticket.

After 3 rejected demos, pause and suggest a short sync to realign on the ACs.

---

## What to do after the ticket is approved

Before Phase 8, confirm that a necessary repository change remains. If investigation or verification showed that no change is needed, return to the solution routing in SKILL.md and finish through the no-code path. Never manufacture a spec-only commit, empty commit, or PR to satisfy this checklist.

### Phase 8: Commits

Only after Gate 4. Conventional Commits (commitlint rules win if present):

```
<type>(<optional scope>): <subject>

<body: what changed and why, wrapped at 72 chars>

Refs: <KEY>
```

Types:
- `feat`: new features
- `fix`: bug fixes
- `docs`: documentation changes
- `style`: formatting, missing semicolons, etc., no logic change
- `refactor`: code refactoring without changing functionality
- `perf`: performance improvements
- `test`: adding missing tests or correcting existing tests
- `chore`: build process, tooling, auxiliary libraries, documentation generation

Rules:
- Subject in imperative mood, lowercase start, no trailing period, header 72 characters max.
- `Refs: <KEY>` footer on every commit so Jira links it. `BREAKING CHANGE: <description>` when applicable.
- Do not use Jira Smart Commit commands (`#comment`, `#time`, `#transition`, `#done`). Ticket state is managed through acli, and smart commits would update it twice or at the wrong moment.
- Atomic commits: one logical change each, tests with the code they cover, OOS fixes and refactors separate.
- Stage by explicit path, review `git diff --cached`. Never `git add -A` blindly.
- Never commit `.env` files, credentials, logs, local config, `.codex/`, or screenshots unless asked.
- Let hooks run. Never `--no-verify`.

Examples:
- `fix(auth): preserve return url when session expires`
- `feat(reports): add csv export for filtered results`

### Phase 9: Audit analysis and optional cherry-picks (GATE 5)

`GATE 5`: use the user's existing choice, or offer command-based audit analysis, inclusion of existing audit commits, or skipping this optional step. Analysis and cherry-picks may be combined when requested. No commit SHAs is a normal analysis-only case, not missing input; request SHAs (or a branch and range) only when the user chooses to include existing commits. Apply the shared authorization rule.

**Command-based analysis**

1. Run the requested non-mutating audit command, for example `npm audit --audit-level=high`, in the relevant project. Use the repository's package manager and supported audit command when none was specified. Do not install or upgrade dependencies, generate a lockfile, or run remediation just to obtain a report; report missing prerequisites or command failures separately from vulnerability findings.
2. Report the exact command, exit status, affected packages and dependency paths, severity, available fixes and likely compatibility impact. Distinguish confirmed applicability from uncertainty. A nonzero exit reporting vulnerabilities is evidence to analyze, not permission to repair them.
3. If fixes are requested as a proposal, present targeted options, trade-offs and verification needed, including deferring or declining remediation. Analysis and proposals do not authorize dependency or lockfile changes. Never require audit remediation merely to complete this gate. If existing ACs or required project checks make a finding blocking, explain that constraint without silently fixing it or claiming checks passed.
4. Treat `npm audit fix` as ordinary dependency remediation, not a critical action: it may run when dependency fixes are already authorized, including through Open All The Gates within scope, without an extra command-specific confirmation. Run it as `npm audit fix --force=false` so inherited npm configuration cannot enable forced updates. Review its dependency and lockfile diff and verify the result; analysis-only requests still do not authorize it.
5. Treat audit remediation with force enabled as a critical action because it can install versions outside declared ranges, including breaking changes. This applies whether force comes from `--force` (or `-f`), an npm configuration file, or an environment variable. Never escalate to it automatically when ordinary fixes leave findings. First show the affected packages, proposed version changes and compatibility risks. Execute only when the user specifically authorizes forced remediation covering those changes; generic fix approval or Open All The Gates alone does not establish that scope. Reuse existing specific authorization without asking again.
6. Implement only remediation within the user's authorized scope; Open All The Gates does not turn an analysis-only request or optional proposal into a fix assignment. Apply the spec and dependency authorization rules to any chosen changes, then repeat relevant verification and demo, commit under Phase 8, and rerun the audit. Report remaining findings honestly.

**Existing audit commits, only when selected**

1. Verify each SHA (`git cat-file -t <sha>`) and show `git log --oneline -1 <sha>` plus the change summary for confirmation under the shared authorization rule.
2. Cherry-pick in chronological order with `git cherry-pick -x <sha>`.
3. On conflict: stop, list conflicted files, explain, propose a resolution, ask before resolving anything non-trivial. Never blindly take one side. `git cherry-pick --abort` is always available.
4. Re-run Phase 6 checks.

Record the selected audit mode, results, any applied changes and deferred findings in the handoff/PR as applicable. Analysis-only completion requires no audit commit; skipping requires no SHAs or cherry-picks.

### Phase 10: Push, pull request and Jira review sync (GATE 6)

`GATE 6`: show the branch, `git log --oneline origin/DEV..HEAD`, base branch, PR title, full PR body, draft or ready, and the Jira actions on approval: move to the configured review status, post the PR comment, fill the ticket description's `Fix:` section with the accepted solution (show the exact text and description change), create any follow-up tickets approved earlier but not yet created. Apply the Gate approval contract; presenting this package does not authorize it. Execute the following only once covered by user approval:

1. `git push -u origin codex/<KEY>-<slug>`. Never force push. If a rebase made it necessary, `--force-with-lease`, only on this `codex/` branch, only with approval.
2. **PR title:** commit format with the key, for example `fix(auth): preserve return url when session expires (ABC-123)`.
3. **PR body:** `references/templates.md`, PR body. The core is "Decisions and reasoning". The Ticket section links to Jira. The follow-ups section lists the created ticket keys.
4. `gh pr create --base DEV` (with `--draft` if chosen). If `gh` is unavailable, give the user title, body and compare URL targeting `DEV`, and post the Jira PR comment only after the user shares the PR URL.
5. Apply the Jira actions, including the required `Fix:` update for bugs and features, using reference section 6. Preserve the ticket template and all other description content. Confirm each action by re-reading the ticket, including the saved Fix text. If the update is blocked or cannot be verified, report it as incomplete.
6. Never merge, never deploy, never move the ticket to a done status. Done happens after review, merge and QA, by the team's process.

---

## Jira sync

| Moment | Action | Approved at |
|---|---|---|
| Work starts | Assign to `@me` if unassigned | Gate 2 |
| Work starts | Transition to config `start` status | Gate 2 |
| Work starts | Start comment | Gate 2 |
| Cannot reproduce | Needs-info comment, optional `blocked` status | Ask at that moment |
| Spec approved | Spec comment | Gate 3 |
| Spec approved | Write drafted ACs into Jira | Gate 3, opt-in |
| OOS findings | Create follow-up tickets linked as "Relates" | Gate 3 or Gate 6, opt-in, listed by name |
| Spec changes after demo | Update spec comment | Gate 4 feedback |
| PR opened | Transition to config `review` status, PR comment | Gate 6 |
| Accepted bug fix or feature | Fill the description's `Fix:` section with the accepted solution | Gate 6 (description edit shown explicitly) |
| After PR | Nothing. Done is the team's call | never |


## Definition of done

- [ ] Ticket fetched from Jira, brief approved, config confirmed
- [ ] Jira shows the ticket assigned and in the start status during work
- [ ] Spec approved, spec comment posted, every AC demonstrated
- [ ] Demo completed and Gate 4 approved directly or through Open All The Gates, no unreviewed Jira changes
- [ ] Lint, typecheck, tests and build pass (or pre-existing failures documented)
- [ ] Regression test for each fixed bug, where test infra exists
- [ ] Commits follow the convention, include `Refs: <KEY>`, pass the ASCII check
- [ ] Audit choice recorded: requested analysis reported, selected commits cherry-picked and verified, or optional audit skipped; any remediation authorized and verified, remaining findings disclosed
- [ ] PR opened with key in the title, reasoning, evidence, follow-ups and rollback notes
- [ ] Jira description's `Fix:` section contains the accepted solution for the bug or feature, saved content verified
- [ ] Jira in the review status with the PR comment, approved follow-ups created and linked
- [ ] Shared completion cleanup performed
