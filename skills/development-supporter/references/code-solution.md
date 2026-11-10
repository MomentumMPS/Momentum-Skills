# CODE SOLUTION NEEDED

Read only after SKILL.md selects this path. All resource paths are relative to the skill root. The main authorization and risk-review contracts govern every checkpoint. Historical Gate numbers are retained for handoffs, not serial approval prompts. Honor a narrower investigation, proposal or local-only endpoint.

## Requested branch setup (before Phase 1)

Use only when named branch creation is itself requested or explicitly requested as a prerequisite. This creates missing refs at existing commits; it does not merge, move/delete existing refs or deploy. An active no-code restriction needs an explicit scope change first.

1. Inspect the repository/remote, requested sources and destinations without changing the checkout. Resolve sources to existing commit SHAs. Do not guess missing inputs. If a destination already matches, report it satisfied; if it differs, report the conflict without modifying it. DEV may be absent when creating DEV is itself requested. Preserve a dirty checkout.
2. At the `Git setup` checkpoint, show the remote, source SHA, destinations and their current states. Check branch-create/push automation for deployment or other side effects. A request naming the missing refs and source normally supplies authorization; do not request another approval for the same creation. Uncovered critical side effects require the main contract's specific authorization. Apply mad-senior only when its risk trigger is met, before consequential external action.
3. Create authorized missing refs using create-only operations that fail if the destination now exists. Do not use an ordinary push that could advance a concurrently created branch. On a race or ambiguous response, re-read before retrying. Matching refs are satisfied; different refs are conflicts. Verify against the intended SHAs and report partial success honestly.
4. At `Git result`, report requested-versus-actual refs, evidence and limitations. Request routine Jira sync through `jira-ticket-supporter` only within the requested endpoint. Give the Jira owner the verified branch-setup outcome and actual limitations; do not invent a PR or publish internal classification labels. Do not mark Done automatically.

If branch setup is the entire task, stop after verified refs, authorized sync and cleanup. No implementation branch, app startup, spec, test/build, commit, audit or PR is required. Do not undo successful creation as automatic rollback. For mixed tickets, proceed to file implementation; ordinary DEV-base requirements remain. Never create DEV as a workaround for an ordinary code ticket.

## File-implementation workflow

| Phase | Work | Historical checkpoint |
|---|---|---|
| 1-2 | Recon, brief, safe setup and start sync | Gate 2 |
| 3-4 | Investigation, suitable verification setup and concise spec | Gate 3 |
| 5-7 | Implementation, checks and acceptance evidence | Gate 4 |
| 8-9 | Commits and any requested audit work | Gate 5 |
| 10 | Final risk review when needed, push, PR and Jira sync | Gate 6 |

Continue through these phases without asking for routine approvals. Pause only for the main contract's uncovered consequential decisions or essential missing inputs. Show useful deliverables in progress; do not produce a gate ledger after each phase.

## Phase 1: Recon and base

1. Read applicable AGENTS.md, README, CONTRIBUTING, package/build manifests, lockfiles, CI, PR template and hook/commitlint config. Inspect environment names and example configuration without printing secret values.
2. Identify relevant commands, runtime, environment/data connections and existing spec conventions. Record the required checks; do not invent a browser, build or test suite for a repository that has none.
3. Verify the local remote host/owner/repository against the intended project, including fork versus upstream; record the intended PR destination. Inspect `git status` and existing branches/PRs for the ticket. Preserve unrelated work. Reuse a branch clearly belonging to the assignment; ask only when ownership or divergence is unclear. With unrelated dirty files, prefer an isolated worktree rather than forcing the user to stash, commit or abort. Do not discard or include those changes.
4. Fetch origin and verify `origin/DEV` (case-sensitive) for new implementation branches. Use its resolved SHA as the baseline. Missing DEV or fetch failure blocks branch creation; never silently fall back to main/master/develop. Keep the recorded baseline for before/after checks even if DEV later advances.

## Phase 2: Brief, branch and environment (checkpoint 2)

Show the concise ticket brief from `references/templates.md`, requested endpoint, classification/source, proposed approach, relevant warnings, repository, branch/base and actual environment risk. Reuse confirmed project config. New mappings must come from verified metadata or user input, not a guess from a custom-field value.

Branch format: `codex/<KEY>-<title-slug>`. Keep the key uppercase, strip a duplicate key prefix from the summary, transliterate to ASCII, lowercase the slug, replace runs outside `a-z0-9` with `-`, trim and cap the slug at 60 characters at a word boundary. Respect `branch_includes_key: false` if configured. For an existing assigned branch, reuse it when safe; do not create a duplicate merely to follow naming rules.

Use a clean checkout or an isolated worktree as appropriate, based on the verified `origin/DEV` commit. For example, in a clean checkout:

```bash
git switch -c codex/<KEY>-<slug> origin/DEV
```

Choose the safest environment capable of establishing the outcome. Inspect connected databases, accounts and outbound integrations: LOCAL can call live services and DEV can contain shared data. Treat STG/PRODUCTION reproduction as read-only unless specific write actions are authorized. Environment selection is not deployment authorization.

For end-to-end work, request routine start sync through `jira-ticket-supporter` within the existing authorization. Give it the meaningful starting context; it decides whether a concise comment adds anything and verifies each authorized write.

## Phase 3: Prepare only the verification environment needed

Use the relevant surface: browser for user flows, API/client tests for backend behavior, CLI/fixture runs for scripts, config validation for CI/IaC, and render/link/content checks for documentation. A non-UI ticket does not require app startup or a browser demo. Static checks alone do not prove runtime behavior.

When runtime setup is needed:
1. Install missing dependencies using the repository's lockfile-respecting command. Apply the main authorization contract to dependency changes; do not upgrade merely to make setup convenient.
2. Use a checked free port. Never kill a pre-existing process. Keep logs outside the repository, record the owned process and read the actual URL from output.
3. Wait for readiness up to 120 seconds. On failure, redact and show the last 40 lines, diagnose and retry at most twice.
4. Apply the entrypoint's browser ownership rule. Verify the served URL/environment and relevant deployed revision or local checkout before attributing UI results to this change. A process listening or HTTP 200 alone does not prove the target flow is ready. Do not call manual steps executed evidence until their result is available.
5. Use an authorized test account/session in the agent-owned connection (or the user's explicitly selected session) and verify its role can reach the requested flow. If authentication is missing, prepare the exact sign-in destination/access needed and ask for only that missing input. Do not copy the user's browser profile, extract credentials, log/commit secrets or use a personal production account for testing. A login page or wrong-role denial leaves acceptance unverified; it is not proof of an application defect.

## Phase 4: Investigate and write the spec (checkpoint 3)

For bugs, start from Jira reproduction steps, comments and attachments. Locate affected code/callers and use history when useful. Reproduce through the actual affected interface or a focused failing test, recording expected/actual results and redacted evidence. After at most three distinct evidence-driven unsuccessful attempts, report missing information instead of guessing a fix or declaring resolution. Offer a needs-info comment only within the authorized communication scope.

Explain the evidenced root cause in a few sentences with file locations. Separate observed facts from hypotheses. For features, compare existing behavior/components/contracts against each AC and identify the actual gap.

Draft a proportionate spec using `references/templates.md`: problem, existing or clearly marked drafted ACs, files/approach, verification per AC, risks and out-of-scope items. A simple fix may need only a short paragraph and a few AC/check bullets. A spec is required; a routine human approval and a separate proposal review are not. If the repo keeps specs, save it there during authorized implementation; otherwise keep it in chat, approved communication scope or PR content.

Classify findings: CRITICAL for blocked main flows, crashes, data loss/corruption, security exposure or wrong results without workaround; MEDIUM for degraded behavior with workaround; SMALL for minor/cosmetic defects. Scope is determined by the ticket's requested behavior and ACs, not severity. Unknown scope stays unresolved, not automatically in scope. Log OOS findings separately and do not fix or ticket them without authorization.

Present the chosen approach and proceed on routine in-scope work. Ask for a decision when a genuine requirements conflict, material scope expansion or critical action remains. Story points can flag a mismatch, but do not silently reduce required ACs to fit an estimate. Apply a mad-senior proposal pass only under the main risk contract, before the risky commitment.

Give `jira-ticket-supporter` a meaningful plan update only when useful and within end-to-end scope. Requirements/AC edits and named follow-ups still need specific authorization. Do not describe an autonomous plan as user-approved.

## Phase 5: Implement

- Make the smallest cohesive change that satisfies the spec; follow existing patterns and avoid drive-by refactors.
- For behavior bugs, add a meaningful failing regression test where test infrastructure exists, then fix it. For features, cover important behavior and failure paths alongside implementation. Do not create tautological tests for copy/docs changes; verify them on their relevant surface.
- Implement in manageable slices mapped to ACs. Report meaningful progress, not every edit.
- Correct in-scope defects and refine implementation details without renewed permission. Revisit the spec and critical-action decision when new evidence changes scope, contracts or risk.
- Chores/docs use this path only for actual repository deliverables. Refactors preserve behavior and run the established relevant suite before/after; run the full suite when project rules or breadth require it. Research normally uses no-code unless a repository prototype is explicitly requested.

## Phase 6: Verify

1. Run required project checks and checks relevant to the touched behavior: lint, typecheck, tests, build and e2e as applicable. Reuse adequate results for the same revision. Broaden testing, start extra containers or repeat a full suite only for a project requirement, changed behavior, failure or unresolved risk; optional assurance is not an extra completion gate. Report unavailable, skipped and failing checks distinctly; do not mark them passed.
2. If needed to attribute a failure, compare against the recorded baseline in an isolated temporary checkout with compatible dependencies. Do not switch away from or overwrite the user's working tree. Document pre-existing failures and whether they block confidence in this change.
3. Rerun reproduction/AC scenarios on the appropriate surface and check affected adjacent behavior. Capture meaningful evidence, with secrets and personal data redacted.
4. Self-review the complete ticket change, including committed, staged, unstaged and relevant untracked files, for defects, debug leftovers, secrets and unrelated changes. A committed diff alone omits uncommitted work.
5. Re-read Jira requirements and decisions. Compare actual content with intake/last verified sync, not just `fields.updated`. Routine own comments do not imply a scope change. Resolve material conflicts before delivery; continue unaffected work.

## Phase 7: Present acceptance evidence (checkpoint 4)

Show each relevant AC as PASS, FAIL or NOT VERIFIED, the evidence, checks, limitations and a plain-language resolution summary for the Jira owner. Use a live browser walkthrough when it proves UI behavior; tests, API/CLI results or rendered artifacts can demonstrate other deliverables. Do not ask the user to approve a passing routine demo before continuing.

If a separate specialist result review is required and its target is ready, perform it now: Ponytail for executable behavior, mad-senior for consequential non-code artifacts. If audit work remains, perform the final result review after that work so the verdict covers what ships. Do not repeatedly review unchanged artifacts. A human review may still be necessary for a subjective product choice the requirements cannot answer; show the concrete choice and continue independent work.

User feedback about implementation defects returns to implementation and affected checks. A clarified requirement updates the spec; genuinely new scope needs a decision. If repeated feedback reveals unresolved expectations, surface the specific mismatch rather than retrying blindly.

Before delivery, confirm a repository change remains necessary. Otherwise reroute to no-code, preserving existing work. Never manufacture a spec-only/empty commit or PR to satisfy a checklist. An explicit local-only endpoint ends with verified local work, without commits/push/PR unless requested.

## Phase 8: Commits

Commit verified work on the ticket's codex/ branch as part of end-to-end delivery. Conventional Commits and repository rules apply. Use imperative subjects, a 72-character header limit unless repository rules differ, and `Refs: <KEY>` in each commit. No Jira Smart Commit commands. Keep logical changes atomic and tests with the code they cover.

Stage explicit paths, inspect the staged diff and let hooks run. Never blindly add unrelated files, secrets, environment files, logs, local `.codex` config or screenshots. Inspect hook changes and rerun affected checks; they can invalidate reviewed behavior. No `--no-verify`.

## Phase 9: Requested audit analysis or commits (checkpoint 5)

Use the user's supplied choice. If no audit analysis or commits were requested, record audit skipped and continue; do not stop to offer an optional gate. No SHAs are needed for analysis-only requests.

For analysis, run the requested non-mutating command using the repository's package manager, such as `npm audit --audit-level=high`. Report command/exit status, affected dependency paths, severity, available fixes, likely compatibility impact and uncertainty. Missing prerequisites are not vulnerability findings; do not install/upgrade or generate a lockfile just to obtain a report.

Analysis or a fix proposal does not authorize remediation. If remediation is in scope, apply only authorized dependency changes and verify their diff and behavior. Run ordinary npm remediation as `npm audit fix --force=false` to avoid inherited force configuration. Never escalate automatically to forced updates. Force via flag/config/environment requires specific authorization of affected packages, versions and compatibility risk. Report remaining vulnerabilities honestly; do not make optional remediation a completion requirement unless an actual AC/project check demands it.

For explicitly selected audit commits, verify each SHA and inspect its changes and scope before cherry-picking chronologically with `-x`. Resolve only understood in-scope conflicts; ask about ambiguous intended behavior or new scope. Do not blindly take one side or abort unrelated work.

After changes, rerun affected Phase 6 checks, refresh acceptance evidence and commit the result. Perform the required final specialist review, if any, on the resulting complete change using the main artifact/risk routing. A prior ready verdict or review of a SHA's summary does not cover changed implementation.

## Phase 10: Push, PR and Jira sync (checkpoint 6)

For an end-to-end assignment, prepare the branch/commit summary, PR title/body/base and exact routine Jira updates. Confirm the final change matches verified evidence and any required reviewer verdict (Ponytail Ship or Mad Senior Ship). Then announce and perform authorized Git delivery without another routine approval; Jira Ticket Supporter alone executes and verifies the Jira portion. If a specific critical action is uncovered, finish the reviewable package first and pause only that action.

1. Recheck the intended remote host/owner/repository, head branch/SHA and base `DEV`; pass an explicit repository selector to supported GitHub operations instead of relying on a fork or cwd default. Push the codex/ ticket branch normally. Never force push without specific authorization. Inspect relevant push automation; branch publication must not silently deploy or cause uncovered critical side effects.
2. Create or update the ticket PR targeting DEV, using the repository template or `references/templates.md`. Include the key in the title, reasoning, evidence, limitations, follow-ups and rollback notes. Use a draft when requested or required by unresolved readiness; a draft does not excuse hiding failed checks. Do not duplicate an existing PR. Read back its actual base repository/owner, base branch, head repository/branch/SHA and URL; reconcile them against the intended destination before reporting delivery. A passing code review does not verify PR routing.
3. If `gh` is unavailable, provide the prepared title/body and DEV compare URL; report PR delivery pending. Do not post a PR-opened claim without a real verified PR URL.
4. Hand the verified outcome, relevant checks, limitations and any real PR reference to `jira-ticket-supporter` for authorized result sync. That owner decides reader-facing wording and placement, preserves requirements and verifies each saved action. Follow-up creation/linking still needs specific authorization.
5. Never merge, deploy or mark Done as an automatic continuation. Report PR readiness, verification and Jira sync accurately and perform shared cleanup.

## Definition of done

For end-to-end file implementation:
- [ ] Ticket/context and requested endpoint established; classification and baseline recorded.
- [ ] Spec and observable ACs supported by evidence; unresolved requirements/critical decisions handled.
- [ ] Required and relevant checks completed, failures/limitations disclosed; behavior fixes have meaningful regression evidence.
- [ ] Review triggers assessed; required reviews cover the final relevant behavior/conclusions with the appropriate ready verdict and resolved blocking findings.
- [ ] Commits/hooks and PR follow project conventions, key/link, scope, evidence and rollback requirements.
- [ ] Requested audit choice completed or optional audit skipped; changes verified and remaining findings disclosed.
- [ ] PR exists against DEV; authorized Jira sync, with results returned and verified by `jira-ticket-supporter`.
- [ ] Existing unrelated work preserved and shared cleanup performed.

For a narrower endpoint, mark only genuinely inapplicable delivery steps as such. Failed or blocked required work remains incomplete, even if the implementation itself is ready.
