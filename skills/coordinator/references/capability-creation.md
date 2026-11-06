# Create a capability only for a concrete gap

Use this reference when the user explicitly requests a new skill/agent, or when existing skills and a focused worker brief cannot adequately handle a requested task and the missing capability is useful beyond one transient assignment. The user's Coordinator policy authorizes relevant reusable skill/agent authoring; it does not authorize unrelated installations, expanded account access or weakened controls.

## Choose the smallest durable addition

- **One-off specialization:** delegate with a clear prompt, scope, evidence and output contract. Do not persist a role merely because a worker needs a name.
- **Reusable knowledge or workflow:** assign a bounded creation task to the installed `skill-creator`. Reuse or improve an existing maintained skill when that avoids overlap. The brief names the observed gap, intended requests, nearby exclusions, sources, destination, constraints, expected result and validation cases.
- **Reusable worker role:** author a narrowly scoped Codex agent TOML when stable instructions/capability settings add value beyond a skill. Prefer referencing relevant installed skills in its instructions over copying their full workflows. A role definition is not an extra permission grant.

Do not create a fleet in anticipation of unspecified tasks. Finish the actual requested work using an adequate existing worker when authoring would delay it without a concrete benefit. Keep authoring and execution separate: review a new capability's instructions before using it, and do not execute untrusted candidate instructions merely to inspect them.

## Codex TOML: verify the installed client first

Inspect the installed CLI version/help and only relevant agent/config keys or files. Never print the full user config, tokens or credential stores. Check current official guidance through `openai-docs` when the installed behavior is unclear or the schema has changed.

Current documentation supports standalone personal agents in `~/.codex/agents/*.toml` and project agents in `.codex/agents/*.toml`. Each defines `name`, `description` and `developer_instructions`; `name` determines the role, not the filename. Avoid built-in names unless intentionally replacing one. Optional model/effort values override resolved inherited values. Omit them unless specifically needed and authorized. Agents inherit parent permissions, provider and MCP servers; putting sandbox/approval overrides in a role does not replace those controls. Supported capability toggles can reduce tool availability. [Custom agents and inheritance](https://learn.chatgpt.com/docs/agent-configuration/subagents)

Minimal example, to adapt to an evidenced role rather than install automatically:

```toml
name = "evidence_checker"
description = "Check material claims against supplied sources without editing or publishing."
developer_instructions = """
Review only the assigned artifact and relevant evidence.
Distinguish observations, assumptions and unresolved questions.
Return source-backed findings, limitations and the next needed decision.
Do not edit files, publish, or take the proposed operational action.
"""
```

The configuration reference also documents `[agents.<name>]` declarations with `description` and `config_file`; relative `config_file` paths resolve from the declaring config. Do not mix registration and standalone formats or assume an arbitrary TOML file is discovered. Scalar `[agents]` settings are reserved names. Preserve existing registrations rather than migrating them gratuitously. [Agent configuration reference](https://learn.chatgpt.com/docs/config-file/config-reference)

Prefer the standalone format when supported so a new role does not require changing global defaults. Use project scope for a project-specific role and personal scope only for a reusable personal role. Project configuration depends on trust and can be skipped in an untrusted project; do not change trust settings merely to enable discovery. [Configuration precedence](https://learn.chatgpt.com/docs/config-file/config-basic)

## Preserve configuration and authority

Before writing, inspect the maintained destination and existing changes. Prepare a narrow diff, preserve unrelated content, avoid name collisions and use the normal filesystem permission mechanism. Do not add model overrides, change global concurrency/defaults, broaden tools, modify provider/MCP credentials, or relax sandbox/approval settings to make the role work. Such changes are a separate concrete decision, not an implication of creating a worker.

A textual read-only instruction is a behavioral constraint, not a new sandbox. Keep the parent session's actual permissions appropriate to the task. A specialized role cannot approve its own critical actions, expand its assignment, or delegate recursively without the coordinator's bounded authorization.

## Validate, then verify availability honestly

1. Parse TOML with an actual TOML parser, check the required fields, unique name, referenced skill paths and only supported keys. Validate against a schema for the correct file type; the root `config.toml` schema is not automatically a standalone-agent schema. [Published root configuration schema](https://learn.chatgpt.com/docs/config-schema.json)
2. Inspect the installed CLI's validation/help facilities before using them. For the inspected local CLI, `app-server --print-startup-config --strict-config` is described as validating startup configuration without launching the server. Avoid displaying its full output; this is not proof that a named agent has been discovered or selected.
3. Walk through an intended task, an adjacent task that should not use the capability, and a failure/permission case. Use safe temporary fixtures. Check that the agent preserves scope, produces usable evidence, reports blockers and cannot authorize its own external actions. Run executable helpers only when needed and within the test authorization.
4. Check the active delegation tool's schema/catalog for named-role selection. A task label is not proof of a TOML role selection. If the runtime exposes no custom-role selector, use a normal worker with the validated instructions in its brief, explicitly describing that as prompt-based delegation rather than claiming the saved role is active.
5. Verify discovery in a fresh supported session when necessary. Do not promise hot reload, change an already-running worker's configuration by editing a file, or launch a paid model test solely to manufacture activation evidence. Report separately: files saved, syntax/instructions checked, discovery verified, and actual role execution verified.

The current collaboration tool surface may differ from the public CLI. Inspect the live tool contract every time; do not invent an `agent_type`, `role`, or configuration-file parameter it does not expose.

## Global Coordinator startup guidance

For the user's explicit preference to start new sessions with Coordinator, add a concise instruction to the active Codex-home `AGENTS.md`, preserving existing preferences. Global discovery uses `AGENTS.override.md` before `AGENTS.md`; later project instructions can override earlier guidance. Codex builds this chain per run, so verify in a fresh session rather than promising an existing chat reload. The default home is `~/.codex`, but another configured Codex home is a separate scope. [AGENTS.md discovery and precedence](https://learn.chatgpt.com/docs/agent-configuration/agents-md)

Apply that startup instruction to the primary/root agent only. A delegated worker must retain its assigned specialist role; it must not bootstrap another Coordinator merely because it inherits global instructions. A root can read and follow Coordinator without spawning a duplicate root agent. Respect explicit current user exclusions, higher-priority instructions and unavailable delegation tools.

This is a local startup convention for clients loading that Codex home, not a guarantee for other hosts, ChatGPT products or running sessions. Preserve existing global overrides rather than deleting them to force activation. Verification should inspect loaded instruction sources or a fresh-session response without changing model, permission or account settings.

Verified against official documentation and local CLI help on 2026-11-04. Recheck client-specific support before future agent/config changes.
