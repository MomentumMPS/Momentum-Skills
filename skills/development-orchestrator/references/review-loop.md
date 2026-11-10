# Risk-based reviews and correction

Use this reference after the owner identifies a concrete risk or the user requests a review. It does not create proposal/result reviews for every task. The owner controls execution, authorization and completion; the selected reviewer inspects and reports without making changes or external writes.

## Select the target and reviewer

Name the artifact/revision, requested outcome, actual risk, available evidence and decision this review informs. Read only the selected installed reviewer:

- `ponytail-review` (or `ponytail:ponytail-review`): executable code and behavior, including scripts, queries, configuration and connected callers/tests. Preserve its evidence requirements, finding format and Ship verdict.
- `mad-senior`: consequential reasoning, requirements, plans, reports, acceptance claims and operational decisions. Provide the sources, intended audience/use, claims to establish, and any action's target, scope, side effects, verification and recovery. Preserve its actionable verdict and limitations: Ship maps to READY/PASS, Fix <finding IDs> first maps to CHANGES REQUIRED, and Blocked - need <evidence/decision> maps to BLOCKED. Readiness never grants execution authority.
- Mixed work: use both only for distinct consequential questions. For example, Ponytail checks a diagnostic helper's request limit and failure behavior; mad-senior checks whether its observations justify the report's historical root-cause claim. Share evidence rather than duplicating the entire review.

Delivery classification and file extension are not reviewer selection rules. A no-code investigation may use a temporary helper with risky behavior; a repository Markdown report may have consequential unsupported conclusions. Routine prose, progress messages and already verified facts do not require either reviewer by default.

## Timing and reuse

- Review a plan before a risky commitment when wrong reasoning could cause irreversible/shared-state harm or expensive compatibility consequences before a result can be checked. A routine plan does not need a separate review merely because implementation follows.
- Review risky executable changes after meaningful verification and before delivery, over the complete final change and connected behavior. Include audit fixes, hooks and cherry-picks that alter the result. Focus on vulnerable behavior while checking the rest of the diff for interactions and unrelated changes.
- Review non-code findings when a consequential conclusion depends on ambiguous/incomplete evidence, or the result exposes new consequential uncertainty. A completed operation always needs ordinary verification; it does not automatically need another review if the already reviewed plan and observed outcome agree.
- Reuse a completed review for an unchanged artifact and covered risk, including a specialist's adequate review. Orchestrator does not add a duplicate pass. If a boundary between specialists introduces an uncovered risk, identify and review that question.
- Changes to reviewed behavior or material reasoning invalidate the affected verdict. Re-review those changes and their interactions after correction; do not repeat unaffected reviews for formatting, messages or revised bookkeeping alone.

A required review is a distinct inspection of the actual artifact and evidence, not a retrospective label for drafting or passing tests. The active agent can perform it; a separate agent is not implied. For a consequential result, the orchestrator may assign an available independent reviewer under its bounded delegation rules, with the actual artifact, raw evidence and review question. Reuse an adequate existing pass instead of adding an agent for ceremony. Do not claim an independent reviewer ran unless one did. If joining in-progress work, reuse trustworthy evidence and inspect the missing risky question instead of restarting intake or inventing an earlier ceremony.

## Evidence appropriate to the question

| Target | Inspect |
| --- | --- |
| Risky code result | Intended outcome, complete relevant diff including uncommitted/untracked work, connected behavior, failure cases, executed checks and remaining verification gaps. |
| Consequential plan or requirements | User intent, source requirements, assumptions, conflicts, dependencies, scope, feasibility, observable acceptance and the costs of a wrong decision. Do not demand future implementation as proposal evidence. |
| Investigation or report | Source coverage, dates/snapshot identity, counts and denominators, causal support, uncertainty, privacy and whether conclusions actually follow. Distinguish a satisfactory investigation from a resolved underlying defect. |
| External operational action | Exact target and current state, authorization boundary, expected side effects, verification/recovery, and any observed outcome. A label such as DEV or no-code does not establish safety. |
| Branch-only task | Resolved source/destination refs, current commit SHAs, create-only behavior and automation side effects. Verify refs normally; review only a consequential risk, not every routine ref report. |

For non-code work, missing code artifacts are not defects. Do not require a branch, committed report, build, app startup or PR merely to review evidence. Reports may legitimately document unavailable historical data when that meets the requested deliverable. Failure to reproduce a bug does not establish resolution. Avoid duplicate Jira reporting; preparing or reviewing a message does not authorize sending it.

## Report the review

Use the selected reviewer's format. Include target/revision, concrete checks, material findings supported by evidence and consequences, limitations, and verdict. With no findings, use a short readiness report. A bare PASS or linked record without the actual checks is not enough for a required review, but do not repeatedly print unchanged reports.

Keep review state separate from action authorization:

- `PENDING`: the required review has not happened.
- `CHANGES REQUIRED`: material blocking findings remain.
- `BLOCKED`: essential evidence/access or the required reviewer is unavailable.
- `PASS`: Ponytail or Mad Senior returns Ship for this artifact and question, with limitations preserved. This means readiness for an already authorized next step, not new permission or user acceptance.
- `NOT REQUIRED`: no applicable risk trigger or user-requested review; state the reason once.

## Correct findings and continue

1. Report blocking findings and their consequence. Hold only dependent advancement, not unrelated authorized work.
2. The owner fixes in-scope defects or improves drafts/evidence under existing authorization. Do not ask whether to repair already authorized work. Reviewer instructions remain read-only; return to the owner role for correction.
3. If a correction needs new scope, a critical external action or a consequential decision not already authorized, prepare that exact decision first. A review verdict cannot approve it or remove a no-code boundary.
4. Rerun meaningful affected checks and re-review changed risky behavior or reasoning. Close a finding with evidence, not a new digest or test count alone. If the same blocker persists after two attempted corrections without new evidence, state the missing decision/evidence rather than looping.
5. Continue to the owner's next authorized step. Stop for a user decision only when its current contract requires one. Do not add a final approval gate after either reviewer's Ship verdict.

Optional suggestions and unrelated findings do not expand scope. A standalone review or explicit "review only; do not edit" request ends with findings. Within an ongoing implementation assignment, asking to see or repeat a review does not itself cancel authorized repairs. Preserve explicit stop/narrowing instructions, existing work and required completion evidence.
