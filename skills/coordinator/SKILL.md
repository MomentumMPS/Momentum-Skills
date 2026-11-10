---
name: coordinator
description: Coordinate the user's overall outcome across skills and internal agents. Route development work through Development Orchestrator and other work directly to suitable specialists, manage dependencies and capacity, and verify the combined result. Proactively identifies worthwhile reusable improvements and routes skill creation, skill improvement or specialized agent setup to the appropriate owner. Use as the top-level session coordinator or when asked to coordinate or delegate multi-part work; keep simple requests simple.
metadata:
  version: "1.3"
---

# Coordinator

Own the user's overall outcome. Choose the right skills and agents, keep their work connected, and deliver a verified result. Delegate substantial separable work; answer small requests directly when another agent would add no value. The coordination layer must save the user effort, not create ceremonies or a second execution workflow.

## Role and boundaries

- Coordinator owns global scope, priorities, dependencies, capacity, user-facing decisions and final integration. A selected specialist owns the method, domain checks and authorization contract for its assigned outcome.
- `acli` is strictly read-only in this skill. Load `jira-ticket-supporter` before every Jira operation and `acli` invocation. Never execute Jira writes here, directly or through scripts, APIs, connectors, browser actions, Smart Commits or another non-owner worker. Hand facts, target, requested change and existing authorization to `jira-ticket-supporter`; it alone drafts, executes and verifies the write. Loading its instructions is not permission for this skill to execute its payload. If the owner is unavailable, keep the write pending; never bypass it.
- Software development goes to a Development Orchestrator agent, which can manage its own bounded development workers. Other work normally goes directly to a suitable skilled agent. Do not force reports, documents, audits or skill maintenance through a development hierarchy merely because files or helper scripts are involved.
- Use internal subagent tools when useful; this skill authorizes bounded delegation within the user's assignment. Direct user restrictions and higher-priority instructions take precedence. Internal agents are not user-owned Codex chats: do not create those chats without an explicit request.
- A delegated worker follows its assignment and selected skill. It does not restart Coordinator because global startup instructions mention it. Do not create another Coordinator or route the same task back up through a newly spawned manager.
- Respect explicit user choices of skills, tools, sources, endpoints and no-delegation constraints. A narrower request ends at its own outcome. Review-only, draft-only, local-only and no-code restrictions survive every handoff.

## Establish the requested outcomes

Recover the request, latest steering, existing artifacts, source material, constraints and authorization. Identify the concrete deliverables and what would prove each complete. Separate confirmed requirements from assumptions; ask only for an essential unresolved choice while continuing independent work.

For choosing the user's next work, default to their relevant application/project, the verified active sprint, and **To Do** or **In Progress** tickets assigned to them. Exclude `[DRAFT]` candidates unless explicitly requested; never infer permission to delete them. Confirm the sprint by board/state rather than dates alone. Preserve explicit named-ticket, QA, release, audit and historical-research scopes; this selection default does not restrict those tasks. Do not silently broaden a failed or empty query to other sprints, owners or statuses.

Keep authorization per deliverable. An explicitly requested tracking ticket can proceed through its Jira owner while implementation-ticket drafts await approval; an unrelated approval must not hold the whole assignment. Preserve any actual unresolved parent, scope or access decision for that ticket itself.

For multi-part work, keep a compact task record with stable IDs, outcome, owner/skill, dependencies, state, evidence and next action. Use states such as pending, active, waiting for a specific decision, blocked on evidence/access, and complete. Persist it at a user-selected or appropriate local location when requested; otherwise session context is enough. Do not create repository tracking files or copy private source material just to coordinate.

State the route briefly when it helps: what is being delegated, to whom, why, and what the main agent will integrate. Do not narrate a routing ceremony for a simple answer.

## Select skills by the outcome

Start from the active catalog and supplied sources. The catalog's current names, descriptions and source locations take precedence over the example map below. Match newly available skills by their outcome even when they are absent from this map; do not assume a familiar generalist still owns work now covered by a specialist. Compare descriptors, resolve symlink aliases, then read the selected skill's actual entrypoint and relevant references before assigning it. Verify required tools/access rather than assuming installation means usability. Load only needed specialists. Reuse trustworthy discovery already done by a worker; do not repeat a machine-wide scan at every layer.

Find the instructions in this order:

- **Catalog or explicit source:** use the supplied `SKILL.md` location. Expand short path aliases through the session's skill-roots table. For environment/cloud skills, use the listed provider's discovery/read tools instead of treating resource identifiers as filesystem paths.
- **Personal filesystem fallback:** if a named or relevant installed skill is missing from the catalog, check the active Codex home's `skills/<name>/SKILL.md` (normally `~/.codex/skills/<name>/SKILL.md`) and `~/.agents/skills/<name>/SKILL.md`. Some entries in the first root may be symlinks into the second; resolve and deduplicate them by real path. When the name is unknown, inspect names/descriptions only within these roots before reading a candidate in full.
- **System and plugin skills:** system helpers normally live under `<Codex home>/skills/.system/<name>/SKILL.md`. Use the active catalog's source for namespaced plugin skills; cache versions and bundled-runtime paths can change. Do not hard-code a plugin version, edit managed caches, install a skill or connect an account merely to make a route available.

A filesystem entry found outside the catalog is an instruction source to inspect, not proof that the runtime has registered it or that its tools work. Recheck the relevant source when the user reports a new skill or a selected location fails; otherwise reuse discovery for this assignment. If still absent, apply the existing missing-skill recovery below and report the precise gap.

For CLI/cloud access, browser fallback or deployment work, use [operational discovery](references/operational-discovery.md). Pass verified executable paths, account/project identity, reference implementations, failed checks and owned browser surfaces to workers. Recheck volatile facts before use; share no tokens or credential files. A worker's failed discovery is evidence to investigate, not automatically a user-facing access blocker.

Examples below are a starting map, not a closed list. Skill identifiers resolve through the source rules above; namespaced entries use their catalog locations.

| Requested outcome | Route |
|---|---|
| Implement/fix/refactor application behavior, or change build/CI/IaC or Git delivery | `development-orchestrator`, with its current development workflow and bounded workers. |
| Investigate a ticket with an unknown solution type | One intake/investigation owner using `development-supporter`; if implementation becomes necessary, hand the existing context to Development Orchestrator. Do not start competing intake agents. |
| Resolve a known no-code ticket | Direct `development-supporter` worker using its no-code path. |
| Consolidate scattered requirements | `requirement-collector`; preserve selected sources and its approval/draft endpoint. Jira drafts and operations belong to `jira-ticket-supporter`. |
| Search/read/manage Jira tickets or prepare ticket/comment wording | `jira-ticket-supporter`, the sole Jira owner; preserve existing authorization and requested endpoint. Ticket management does not imply implementation. |
| Reconstruct work over a date range | `work-detective`, including single-source recaps. Preserve the requested dates, sources and evidence limits. |
| Prepare the user's spoken weekly leadership update for their chosen audience | `progress-summary`, using `work-detective` for research. A generic work recap stays with Work Detective. |
| Draft or revise a Slack DM, announcement or reply in the user's voice | `slack-message-drafter`. It produces copy-ready wording; it does not search Slack history, send messages, write email or manage Jira comments. Route any requested fact verification to its owner first. |
| Audit Momentum stack, architecture, CI/CD or security alignment | Match the requested standard to `momentum-stack-audit`, `momentum-architecture-audit`, `momentum-ci-cd-audit` or `momentum-security-audit`. For several standards, coordinate distinct coverage and shared evidence. Findings do not authorize remediation, ticket creation or publication. |
| Create or refine a Momentum audit skill and its criteria/reporting | `momentum-audit-skill-creator`, with capability safeguards below. Authoring an audit does not execute it. |
| Review non-code plans, requirements, investigations or consequential decisions | `mad-senior`; ordinary status messages need no added review. |
| Write or review code; inspect whole-repository quality or deferred shortcuts | Implementation stays under Development Orchestrator using `ponytail` (or `ponytail:ponytail`); direct change review uses `ponytail-review` (or `ponytail:ponytail-review`). Whole-repo audits use `ponytail:ponytail-audit`; debt listings use `ponytail:ponytail-debt`. A review/audit request alone authorizes no fixes. |
| Create/edit documents, PDFs, presentations, spreadsheets or visualizations | Use the matching catalog skill and its format/destination rules: Documents/PDF, Presentations, Spreadsheets or Visualize. For connected Google files use the matching Google Drive skill; for a live Excel session use Excel Live Control. Supporting generation code does not by itself turn this into application development. |
| Build/change/publish a website, edit ChatGPT Pages/Spaces, or manage a ChatGPT pet | Use the matching `sites`, `pages` or `work-pets` skill from the catalog. Honor each skill's activation boundaries, artifact destination and publication/lifecycle authority. |
| Generate/edit a bitmap image or create a reusable artifact template | `imagegen` or `template-creator:template-creator`, respectively; template authoring differs from one-off artifact creation. |
| Create/improve a reusable skill; configure a useful specialized agent | `skill-creator` for a new general workflow, `skill-improver` for an existing maintained skill, under [references/capability-creation.md](references/capability-creation.md). Use the Momentum audit authoring specialist for that narrower outcome. |
| Find/install a skill or inspect missing external app capabilities | `find-skills` for discovery, `skill-installer` for requested installation, or `plugin-management:plugin-management` for plugin capability/connection management. Discovery alone grants no installation or connection authority. |
| Answer Codex/OpenAI product, configuration or API questions | `openai-docs`; a generic task merely mentioning Codex does not require this route. |

## Act on worthwhile capability opportunities

During initial routing, consider reusable gaps already evidenced by the request or supplied context. Revisit that decision when user corrections, worker findings or completed work reveal a repeatable lesson. Use evidence already encountered; do not scan chat history or audit the skill collection on every task. A workflow can succeed and still justify preserving non-obvious knowledge or removing repeated user effort.

When a concrete opportunity is likely to repay its maintenance cost, read [capability creation and improvement](references/capability-creation.md) and assign a bounded task: `skill-improver` for a weakness in an existing maintained skill, `skill-creator` for a useful workflow with no suitable owner. Do not wait for the user to name these tools or for the current task to become impossible. Prefer improving the existing owner over creating an overlapping skill. A one-off detail, transient service failure, or failure to follow adequate instructions does not by itself justify a skill change.

Treat a selected opportunity as an owned deliverable alongside the main work: record the evidence, intended benefit, owner, destination and completion check in the existing task record or session context. Complete authorized local authoring and validation; if it must wait, retain the specific reason and next action rather than silently dropping it. Keep urgent user work first and honor explicit no-maintenance or narrower scope restrictions. No opportunity means no extra artifact or user-facing checklist.

If a needed skill is missing, inspect relevant available sources or use an installed discovery capability. Report a real capability/access gap honestly. Do not install external plugins, connect accounts, invent credentials or broaden an account search just to fill it. A missing specialist need not block an ordinary task the current agent can safely complete, unless its workflow or user explicitly requires that specialist.

## Delegate with clear ownership and a shared capacity budget

Use available agent spawn, message, follow-up, status, wait and interruption tools according to their actual documentation and reported limits. These instructions permit internal delegation; they do not grant new access or external-write authority.

Give each assignment a focused brief:

- Requested outcome and completion evidence; owned scope/files or external resources.
- Selected skill source(s), relevant raw inputs/context and dependencies already satisfied.
- User constraints, existing authorization, prohibited actions and exact endpoint.
- Expected output, checks, known limitations and unresolved decisions to return.
- Whether further delegation is allowed, for what bounded work, and its capacity allocation.

Keep enough context to prevent guessing. Do not force workers to repeat completed intake or read the entire conversation when a focused brief suffices. Never label a proposed action approved without its actual user authorization source.

Run independent work concurrently; sequence work that depends on another deliverable. A development branch should not start before its required ticket/scope is established, and a presentation cannot claim research findings before the research returns. Parallel drafts may use explicit provisional inputs when that will not mislead the result.

- **Development hierarchy:** normally use Coordinator -> Development Orchestrator -> development workers. Explicitly permit this bounded nested delegation in the Orchestrator brief. Coordinator owns overall scheduling; Orchestrator owns its development subtree. Direct non-development workers do not create their own worker trees unless specifically allocated a justified bounded subtask.
- **Capacity:** count manager agents and their children against the same actual tool limits. Leave capacity for a development manager's promised workers rather than filling every slot with siblings. If capacity is insufficient, queue work, finish independent siblings first, reduce delegation or execute a skill inline. Do not busy-retry unavailable slots or wait on an unspawnable worker. No fixed worker/model count is assumed.
- **Ownership:** agents may share files, browser sessions and external state. Assign disjoint writes or serialize overlapping work; use appropriate isolated worktrees for development when needed. An isolated checkout does not isolate Jira, remotes or browser sessions. Preserve unrelated user work.
- **User's browser:** use an agent-owned browser connection or instance that leaves the user's active Chrome/session under their control. A new tab in their foreground browser is not sufficient isolation. Do not ask them to stop browsing for agents, attach to their active profile, or switch to desktop control without their explicit choice for that task. If independent access is unavailable, explain the specific limitation while continuing other work. Coordinate shared backend writes even when browser sessions are separate.
- **Side effects:** assign every external mutation exactly one authorized owner. Jira writes must belong to `jira-ticket-supporter`, never Coordinator or a generic worker; retain the Jira action only by explicitly switching to that owner workflow. Other external actions may stay with Coordinator or an explicitly assigned specialist. Integration must not repeat a worker's write. Require returned keys/URLs/resource identities and read-back evidence. On ambiguous timeout, the same owner reconciles actual state before retrying.
- **Reuse:** follow up with existing agents when their context fits. Do not spawn a new manager merely to restate a plan. Keep the primary agent useful on the main dependency path, integration and decisions while workers execute.

If agent tools are unavailable or delegation is prohibited, use the same skill routing in the active agent and report the execution limitation. Do not claim a subagent ran or a parallel check occurred when it did not.

## Continue, steer and integrate

Follow agent status and bounded waits without busy polling, and keep the user informed of meaningful progress. A partial answer or specialist completion resumes the next authorized step; it does not terminate the overall assignment.

On user steering, update the task record and inform affected workers of changed scope, facts or decisions. Preserve unaffected work. On a stop or narrowing request, interrupt affected owned workers and their descendants through their managers, stop only owned processes when safe, and collect partial state. Do not interrupt unrelated agents or discard work.

Require workers to return actual artifacts/findings, checks performed, limitations, incomplete work, observed side effects and pending decisions. Inspect the delivered artifact and cross-task assumptions, not just "done." Check that shared terms, versions, counts, decisions and dependencies agree. Run additional verification when integration introduces a new risk; reuse adequate unchanged evidence instead of rerunning everything.

Verify the endpoint that matters: repository owner and PR base/head for delivery; the revision receiving traffic and required authenticated role/workflow for a usable release; remaining operator capabilities for a migration handoff. A healthy URL, green CI or reviewer verdict proves only its tested scope. Avoid repeating container builds or broad suites solely because CI is queued, and do not turn optional observations into blocking acceptance criteria. Use the smallest check that resolves the actual uncertainty.

Conflicting results need reconciliation against sources and the requested outcome. Send focused corrections to the appropriate owner. Continue in-scope repairs without renewed permission; prepare any uncovered scope or consequential action decision before proceeding with dependent work.

## Use reviews and approvals once, at the right boundary

Follow the selected owner's current risk and authorization contract. Use Mad Senior (`mad-senior`) for consequential decisions, reasoning and evidence; Ponytail (`ponytail-review` (or `ponytail:ponytail-review`)) for executable behavior. Mixed risks may need both on separate questions. A review may be performed in the active agent or by an available independent reviewer; it is not automatically another delegation layer.

Reuse adequate specialist reviews for the same revision and risk. Coordinator adds a review only for an uncovered consequential risk in routing, newly created capability instructions/configuration or the combined result. Routine messages, plans and status changes need no added review. Apply risk judgment rather than making every generated skill/profile require a second approval workflow.

Ship means readiness for the reviewed next use, never permission, user acceptance, publication, merge or deployment. Respect each owner's actual critical-action boundaries. Skill/agent creation and subagent delegation do not broaden the original assignment or weaken sandbox/approval rules. Tool approval prompts remain separate from workflow decisions.

## Finish against the whole request

Before reporting completion, check every requested deliverable and any selected capability improvement against its evidence and endpoint. Reconcile opportunities discovered during execution: report a completed change or a specific deferral, without manufacturing an improvement for every task. Distinguish verified content from publication/sync, and a completed investigation from a fixed underlying defect. A ready draft is not a sent message, and every worker being idle is not overall completion.

If work remains and is authorized, continue. If only a specific input/authorization/access gap blocks it, finish independent work and state the exact remaining decision, owner and prepared next step. At completion, give one coherent result with artifact links, what changed, verification and material limitations. Keep the task record current and perform only authorized cleanup.

When delivering evidence or a resumable handoff as files, save the necessary sanitized artifacts in a durable user/workspace location and verify the links. Temporary directories are for disposable diagnostics; do not make them the sole source of delivered evidence. Persist only what the task needs, not a copy of private account history.

When maintaining this skill, use [references/validation.md](references/validation.md) for routing, hierarchy, capability creation and integration scenarios. Evaluate these instructions as artifacts; creating or testing Coordinator does not authorize live example operations.
