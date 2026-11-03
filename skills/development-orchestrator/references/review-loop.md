# Proposal and result reviews

Load the installed Ponytail Review instructions. Use their priorities, evidence requirement, finding groups and four-part explanations. Reviewing is read-only; the workflow owner makes authorized corrections. Always name the target and its revision so Ponytail does not default to the last commit or an unrelated diff.

## Separate review of the completed artifact

After drafting, review the actual completed proposal as a separate pass with `ponytail-review` (or `ponytail:ponytail-review` when installed as a plugin), before calling it ready for human approval. Earlier source inspection, baseline tests and the general `ponytail` skill are not that review. Identify the proposal revision and report checks, findings, limitations and verdict. If a review record is absent on resume, keep it PENDING and perform the review; never reconstruct a PASS from drafting notes. If already approved by the user, preserve that authorization for unchanged scope but complete the missing review before dependent execution. Corrections that materially change the proposal reopen the affected human decision.

Apply the same separation to results: after implementation and verification, announce the Ponytail review target and inspect the completed artifact and connected behavior in a distinct read-only pass. The active agent can perform it; no separate agent or tool invocation is implied. Follow the installed review skill, rather than merely naming its checklist in a retrospective record. Challenge the relevant failure paths against the actual sources; passing test totals and fixes found during implementation are supporting evidence, not the review itself. After any correction, review the affected behavior in the revised artifact before issuing PASS; changing a report's digest or test count alone does not renew its verdict.

## Choose the evidence for the selected path

| Review | Input and checks | Return defects to |
| --- | --- | --- |
| Code proposal | Spec, acceptance criteria, cause/gap evidence, affected code/callers and planned checks. Check correctness, security, load, meaningful tests, reuse and scope. Missing future implementation/tests are expected, not findings. | Investigation/spec phase, then proposal review and affected human approval. |
| Code result | Approved spec, complete ticket diff including committed, staged, unstaged and relevant untracked files, connected callers/callees, and actual check/demo evidence. Separate unrelated edits; do not change uncertain ownership. | Implementation, affected verification and result review; revisit the proposal if the design changes. |
| No-code proposal | Requested outcome, source set or investigation method, evidence already available, proposed external action if any, target/environment, authority, risk, verification and reversal when relevant. Verify the method can answer the question and the action addresses the evidenced cause. | N1 investigation/action proposal; obtain only the approval the selected workflow requires. |
| No-code result | Findings or observed action results, evidence for each acceptance criterion, source coverage and limitations, current ticket requirements, exact proposed comment/Fix/description/transition when applicable. Check conclusions follow from evidence and do not overclaim resolution. | Missing investigation or authorized correction, verification and review before N2 acceptance/sync. |
| Branch setup | Proposal: exact repository, source/destination refs and commits, existing destination state and automation side effects. Result: requested-versus-observed refs and verification. | The bounded Git setup/result procedure, never file implementation solely for evidence. |

Plans and non-code artifacts are explicit adaptations of Ponytail's code-change review. Inspect relevant source documents, logs, queries, settings or existing behavior instead of demanding a code diff. Use the same plain-English finding format, citing actual sections/evidence rather than invented line numbers. State the environment or usage scale assumed when relevant. `What this change does:` describes proposed work or the non-code outcome honestly; `Ship` means review readiness only.

For a read-only investigation, review a short approach without requiring a repository spec or user approval just to read authorized sources. If joining an investigation already in progress, review the actual method/evidence and fill gaps; do not redo completed work merely to stage a proposal. No-code work never needs a synthetic branch, commit, build, app startup, or PR. A dirty existing checkout is preserved and does not prevent read-only review.

For non-code reports, distinguish a verified deliverable from an unresolved underlying question. If the acceptance criteria permit documented unavailable data, assess the report on that basis. Failure to reproduce a bug does not establish resolution. Existing adequate reporting need not be posted again. Ticket creation keeps Fix blank; completed resolution fills it only when the selected workflow calls for it and the exact write is authorized. Approval to post findings alone does not authorize a description edit or status transition.

## Produce a real review record

Record the reviewed artifact/revision or precise evidence snapshot, checks actually performed, concrete findings with stable IDs, limitations, verdict and next boundary. A bare "Plan review: PASS" or "Ponytail approved" without the target and checks is not a completed review. Do not claim an independent reviewer or tool ran if the active agent performed the review itself.

Deliver the review in chat using Ponytail's output format: `What this change does:`, nonempty finding groups with the four-part explanations and evidence, verdict, and material limitations. Include the reviewed target/revision and checks; with no findings, use its short no-findings format. A file can retain supporting detail but cannot replace this report. For an internal review with blockers, show the findings in commentary, then continue authorized correction in the same turn. Report closure evidence and the new verdict after re-review; do not end at the initial findings or ask for gate approval while they remain open.

- `PENDING`: this artifact has not been reviewed.
- `CHANGES REQUIRED`: concrete blocking findings or required criteria/checks fail.
- `BLOCKED`: review cannot be completed because required evidence, access, a dependency or a decision is missing.
- `PASS`: the review returns `Verdict: Ship.` or `Looks good. Ship.` for this artifact, and the verification applicable at this stage is sufficient under the owning workflow's rules. Planned tests need not exist at proposal time. Documented pre-existing failures and explicitly allowed research limitations retain their proper treatment.

## Automatic correction at every orchestration section

Whenever an internal Ponytail review returns Must fix findings or names other findings that block its Ship verdict, start correction in the same turn. This applies to discovery/routing artifacts, requirements, ticket drafts, specifications, code, non-code plans/findings, branch setup proposals, and delivery packages whenever those artifacts are reviewed within the assignment. It does not require creating a new review checkpoint for every trivial action.

1. Record `CHANGES REQUIRED`, the reviewed revision, stable finding IDs, failing cases and smallest fixes. Hold dependent advancement; do not ask "Should I fix these?" for corrections already inside the user's authorized scope.
2. Route each correction to the owning specialist. Ponytail remains read-only during the review pass; the owner performs the authorized changes, then returns the revised artifact to Ponytail. Report-only behavior of the reviewer must not terminate the orchestrated assignment.
3. Correct drafts or proposals before presenting the relevant approval gate. Correct implementation only when the applicable implementation approvals already cover it. For non-code work, correct reasoning, evidence or drafts as authorized; an operational repair or Jira write still needs its own existing authorization. No-code scope never becomes permission for repository edits.
4. If a correction requires new scope, a material plan change, a dependency change, installation, or an external write not already authorized, prepare the concrete correction and leave only dependent work blocked for that decision. Do not treat the review verdict as permission, bypass a human gate, activate Open All The Gates, or manufacture consent. Respect the owner's rules for independent work while waiting.
5. Rerun meaningful affected checks and review the changed artifact and connected behavior. Close a finding only with evidence that its failing case is resolved. Repeat until PASS or a real blocker, then continue to the next applicable workflow step or human gate.

Optional Should fix/Nice to have suggestions and unrelated findings are not automatic scope expansion. A finding in a Ship-blocking verdict still requires either an authorized correction or an explicit scope/blocker decision; do not silently drop it. A standalone review request or an explicit narrowing such as "review only; do not edit" preserves that limit. During an authorized solution workflow, "Why didn't you review it?", "Use Ponytail Review", or "Show the result in chat" requests review evidence, not cancellation of authorized repairs. Show the report and resume the owner correction loop. An unapproved result-acceptance gate does not revoke the earlier implementation approval for in-scope defect repairs; it still blocks the actions that require result acceptance.

Continue until PASS or a real blocker. If the same blocker survives two attempted corrections without new evidence, pause that work and present the unresolved decision/evidence needed. Respect stricter retry limits in the owning skill, including rejected demos. Do not count internal review rejection as a human demo rejection or stop merely because several productive revisions were necessary.

## Handoff after review

On PASS, prepare the complete next applicable human gate, including the concrete artifacts and proposed writes. Wait only for uncovered authorization. With valid scoped approval or applicable standing approval, execute and verify the authorized next step; do not stop at the review report in an end-to-end assignment.

Review cannot replace the owner's verification, demo, evidence acceptance, write checks or cleanup. Recheck the final deliverable against the reviewed snapshot before delivery. Changed code, non-code evidence, configuration targets or proposed writes require the affected review and approval to be revisited. Keep review status separate from authorization throughout.
