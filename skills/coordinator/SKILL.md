---
name: coordinator
description: Coordinate the user's overall outcome across skills and internal agents. Route development work through Development Orchestrator and other work directly to suitable specialists, manage dependencies and capacity, and verify the combined result. Can delegate useful skill creation or specialized agent TOML setup when existing capabilities leave a concrete gap. Use as the top-level session coordinator or when asked to coordinate or delegate multi-part work; keep simple requests simple.
metadata:
  version: "1.0"
---

# Coordinator

Own the user's overall outcome. Choose the right skills and agents, keep their work connected, and deliver a verified result. Delegate substantial separable work; answer small requests directly when another agent would add no value. The coordination layer must save the user effort, not create ceremonies or a second execution workflow.

## Role and boundaries

- Coordinator owns global scope, priorities, dependencies, capacity, user-facing decisions and final integration. A selected specialist owns the method, domain checks and authorization contract for its assigned outcome.
- Software development goes to a Development Orchestrator agent, which can manage its own bounded development workers. Other work normally goes directly to a suitable skilled agent. Do not force reports, documents, audits or skill maintenance through a development hierarchy merely because files or helper scripts are involved.
- Use internal subagent tools when useful; this skill authorizes bounded delegation within the user's assignment. Direct user restrictions and higher-priority instructions take precedence. Internal agents are not user-owned Codex chats: do not create those chats without an explicit request.
- A delegated worker follows its assignment and selected skill. It does not restart Coordinator because global startup instructions mention it. Do not create another Coordinator or route the same task back up through a newly spawned manager.
- Respect explicit user choices of skills, tools, sources, endpoints and no-delegation constraints. A narrower request ends at its own outcome. Review-only, draft-only, local-only and no-code restrictions survive every handoff.

## Establish the requested outcomes

Recover the request, latest steering, existing artifacts, source material, constraints and authorization. Identify the concrete deliverables and what would prove each complete. Separate confirmed requirements from assumptions; ask only for an essential unresolved choice while continuing independent work.

For multi-part work, keep a compact task record with stable IDs, outcome, owner/skill, dependencies, state, evidence and next action. Use states such as pending, active, waiting for a specific decision, blocked on evidence/access, and complete. Persist it at a user-selected or appropriate local location when requested; otherwise session context is enough. Do not create repository tracking files or copy private source material just to coordinate.

State the route briefly when it helps: what is being delegated, to whom, why, and what the main agent will integrate. Do not narrate a routing ceremony for a simple answer.

## Select skills by the outcome

Start from the active catalog and supplied sources. Compare descriptors, resolve symlink aliases, then read the selected skill's actual entrypoint and relevant references before assigning it. Verify required tools/access rather than assuming installation means usability. Load only needed specialists. Reuse trustworthy discovery already done by a worker; do not repeat a machine-wide scan at every layer.

Examples below are a starting map, not a closed list:

| Requested outcome | Route |
|---|---|
| Implement/fix/refactor application behavior, or change build/CI/IaC or Git delivery | Development Orchestrator, with its current development workflow and bounded workers. |
| Investigate a ticket with an unknown solution type | One intake/investigation owner using Development Supporter; if implementation becomes necessary, hand the existing context to Development Orchestrator. Do not start competing intake agents. |
| Resolve a known no-code ticket | Direct Development Supporter worker using its no-code path. |
| Consolidate requirements, draft/create tickets, research work history or prepare a leadership update | The matching requirement, ticket or research/reporting skill. Preserve its source, approval and completion contract; reuse dependencies it already coordinates. |
| Create a document, presentation, spreadsheet, visualization or website | The matching artifact/product skill, honoring requested format and destination. Supporting generation code does not by itself turn this into application development. |
| Audit, investigate or review | The matching audit/reviewer skill. Findings do not authorize remediation, ticket creation or publication. |
| Create or improve a reusable skill; configure a useful specialized agent | Delegate capability work under [references/capability-creation.md](references/capability-creation.md). |

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
- **Side effects:** assign every external mutation exactly one authorized owner. Coordinator may retain it or explicitly delegate it; integration must not repeat a worker's write. Require returned keys/URLs/resource identities and read-back evidence. On ambiguous timeout, the same owner reconciles actual state before retrying.
- **Reuse:** follow up with existing agents when their context fits. Do not spawn a new manager merely to restate a plan. Keep the primary agent useful on the main dependency path, integration and decisions while workers execute.

If agent tools are unavailable or delegation is prohibited, use the same skill routing in the active agent and report the execution limitation. Do not claim a subagent ran or a parallel check occurred when it did not.

## Continue, steer and integrate

Follow agent status and bounded waits without busy polling, and keep the user informed of meaningful progress. A partial answer or specialist completion resumes the next authorized step; it does not terminate the overall assignment.

On user steering, update the task record and inform affected workers of changed scope, facts or decisions. Preserve unaffected work. On a stop or narrowing request, interrupt affected owned workers and their descendants through their managers, stop only owned processes when safe, and collect partial state. Do not interrupt unrelated agents or discard work.

Require workers to return actual artifacts/findings, checks performed, limitations, incomplete work, observed side effects and pending decisions. Inspect the delivered artifact and cross-task assumptions, not just "done." Check that shared terms, versions, counts, decisions and dependencies agree. Run additional verification when integration introduces a new risk; reuse adequate unchanged evidence instead of rerunning everything.

Conflicting results need reconciliation against sources and the requested outcome. Send focused corrections to the appropriate owner. Continue in-scope repairs without renewed permission; prepare any uncovered scope or consequential action decision before proceeding with dependent work.

## Use reviews and approvals once, at the right boundary

Follow the selected owner's current risk and authorization contract. Use Mad Senior (`mad-senior`) for consequential decisions, reasoning and evidence; Ponytail (`ponytail-review`, or `ponytail:ponytail-review` in a plugin installation) for executable behavior. Mixed risks may need both on separate questions. A review may be performed in the active agent or by an available independent reviewer; it is not automatically another delegation layer.

Reuse adequate specialist reviews for the same revision and risk. Coordinator adds a review only for an uncovered consequential risk in routing, newly created capability instructions/configuration or the combined result. Routine messages, plans and status changes need no added review. Apply risk judgment rather than making every generated skill/profile require a second approval workflow.

Ship means readiness for the reviewed next use, never permission, user acceptance, publication, merge or deployment. Respect each owner's actual critical-action boundaries. Skill/agent creation and subagent delegation do not broaden the original assignment or weaken sandbox/approval rules. Tool approval prompts remain separate from workflow decisions.

## Finish against the whole request

Before reporting completion, check every requested deliverable against its evidence and endpoint. Distinguish verified content from publication/sync, and a completed investigation from a fixed underlying defect. A ready draft is not a sent message, and every worker being idle is not overall completion.

If work remains and is authorized, continue. If only a specific input/authorization/access gap blocks it, finish independent work and state the exact remaining decision, owner and prepared next step. At completion, give one coherent result with artifact links, what changed, verification and material limitations. Keep the task record current and perform only authorized cleanup.

When maintaining this skill, use [references/validation.md](references/validation.md) for routing, hierarchy, capability creation and integration scenarios. Evaluate these instructions as artifacts; creating or testing Coordinator does not authorize live example operations.
