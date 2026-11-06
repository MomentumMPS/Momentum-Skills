# Discover and select skills across hosts and products

Build knowledge from observed installations, not a hardcoded four-skill list. Inventory all skill descriptors in the accessible, relevant skill roots, then read the full instructions and dependencies of candidates needed for the current outcome. Keep that distinction explicit: indexed metadata is not a claim to have read every skill or to have access to every machine.

## Persistent inventory and scan triggers

Store the inventory outside repositories and distributed skill files, at `$XDG_STATE_HOME/development-orchestrator/skill-inventory.json` when that user-state location is configured, otherwise `~/.local/state/development-orchestrator/skill-inventory.json`. Use an existing user-specified inventory location instead when supplied. On hosts without persistent filesystem access, use a supported user-scoped storage mechanism if available; otherwise disclose that only session memory is available. Never claim persistence unless the saved data can be read back.

For an installation renamed from `leviathan-orchestrator`, reuse its existing private inventory at the legacy state location when present. Do not reset or duplicate that inventory merely because the skill name changed; migrate it only through an explicitly selected storage change.

- On first use, load the saved inventory. If it is missing, invalid, or has no skill entries for the current host/product/project scope, run discovery once for that scope and persist the results. An empty or inaccessible scan is a coverage result, not a reason to loop repeatedly in the same invocation.
- On subsequent uses with saved entries, load them without a full automatic rescan. Verify the selected skill's current source and required capabilities before use. A new host or project scope gets its own initial discovery; it does not reuse another machine's activation claims.
- A direct request to scan or rescan overrides cache reuse at any time. Scan the requested sources, update the inventory, report additions/changes/removals and coverage gaps, then resume the original task unless the user changed its scope. A scan does not approve a pending work gate.
- When the active catalog reveals a new skill, a selected entry changes, or a capability gap requires discovery, inspect and persist those entries incrementally. Do not turn a single missing dependency into an unrelated full-machine scan.

Keep a versioned JSON inventory containing host/product/project scope, scanned roots and coverage errors, scan time, and skill name/namespace, description, version when declared, canonical path/resource, aliases, observed availability, and last verification time. Store metadata only, never credentials, approval history, ticket content, or copied skill instructions. Cached availability is a hint, not proof of current access or authorization.

Update atomically using a temporary file in the same state directory and replacement. Preserve unrelated scopes and any entries updated since loading by re-reading before merging. Remove an entry only when its source was successfully scanned and its absence confirmed; do not erase good records because a host or root is temporarily inaccessible. If persistence fails, report the failure, retain results in session, and continue independent authorized work within host permissions. Discovery records skills; it does not install or execute them.

## Inventory the current environment

1. Start with the session skill catalog, its root mappings, tool metadata and any supported skill/plugin listing APIs. Record product, host, namespace, path/resource, description, version when declared, and availability. Use the provider's documented list/read mechanism for managed or remote resources.
2. Supplement the catalog with read-only filesystem discovery in confirmed skill locations. Cover user, project, system/admin and installed plugin sources that are accessible. On a filesystem, prefer `rg --files --hidden -L -g SKILL.md <confirmed-roots>`; inspect errors and enumerate inaccessible roots separately. Inspect product command/agent inventories separately when they can provide a needed capability; they are not automatically SKILL.md skills.
3. Read each discovered manifest's metadata to update the compact persistent capability index and its session view. Preserve namespaces and distinguish duplicate names; collapse symlink aliases by resolved path while retaining product/host locations. Do not silently choose the newest cached version over the active catalog or explicit user source. Record uncertain activation instead of guessing.
4. Load relevant candidates completely: SKILL.md, referenced workflow sections, tool dependencies, resource locations, approval rules, side effects and output contracts. Compare inputs/outputs and constraints before composing skills. Match the requested outcome, not superficial keywords. Record the chosen owner/specialists and why each is needed.
5. Save and read back the updated inventory under the persistence rules above. State coverage and gaps; do not claim an exhaustive machine inventory from the prompt catalog alone. Reuse saved entries on later runs, with targeted verification and updates as needed.

Typical discovery roots are starting points to verify, not promises about the active product:

| Source | Places to inspect when accessible |
| --- | --- |
| Codex/shared user skills | Session catalog paths, the configured Codex home skills directory, `~/.codex/skills`, `~/.agents/skills`, and applicable `.agents/skills` directories in the project hierarchy. |
| Codex system/plugin skills | Catalog-provided system and plugin roots; confirmed admin paths such as `/etc/codex/skills`; plugin listing metadata for installed/enabled versions. |
| Claude Code | `~/.claude/skills`, applicable project `.claude/skills`, explicitly configured additional/managed directories, and skill roots of installed plugins. Inspect legacy `.claude/commands` or agents only as separate capabilities when relevant. |
| Other products | Use their installed configuration, documented listing APIs, CLI help, or an appropriate discovery skill to locate actual roots. Do not assume Codex or Claude conventions apply. |
| Another machine | Use an available authorized host connection and its catalog/read-only file tools, or a user-supplied exported inventory. Identify host and product on every result. |

Files in a plugin marketplace checkout or an old cache prove availability on disk, not installation, enablement, or usable tools. Label them as candidates until verified. Avoid traversing the entire home directory, scanning the network for machines, reading credential stores, or printing unrelated configuration. Inspect relevant skill/plugin metadata only. If a root is missing or unreadable, report that coverage gap; an error is not an empty inventory.

## Fill a capability gap

Use installed `find-skills` when no adequate local candidate exists or the user asks for broader discovery. Follow its current search procedure, including the skills.sh leaderboard before CLI search, and inspect the actual candidate instructions/source before recommending it. Popularity is supporting evidence, not a substitute for fit, permission boundaries and compatibility. Check current CLI help before using commands or flags; `npx skills list` can supplement installed-skill discovery and `npx skills find <query>` searches the ecosystem. A public search does not inventory a private remote machine.

If find-skills cannot access a requested product/host, look for an installed discovery, remote-management or plugin-management capability suited to that environment. Use it only within available connection permissions. If no access exists, request the specific host connection, skill root, or exported inventory needed while continuing local analysis. Do not invent remote availability, automatically connect to unknown hosts, or promise access to Claude account/cloud skills from a local directory alone.

Distinguish discovery, compatibility inspection, installation and execution. Searching does not authorize installing, updating, removing or syncing skills, starting another agent product, or executing scripts/hooks from a discovered skill. Propose the concrete source, destination, dependencies and required changes when installation/adaptation is needed; honor existing user authorization without redundant confirmation. Use an appropriate installer/authoring skill for authorized changes.

When a required owner or the selected reviewer is missing, report the dependency and continue independent discovery/read-only preparation. Load Ponytail Review or mad-senior only for an applicable review trigger; an unused reviewer is not a blocker. Do not replace its contract with a guessed workflow or report a review as passed. Alternatives can be proposed with their tradeoffs, but the human must authorize a change to a required workflow.

## Cross-product compatibility

Shared Markdown instructions may be usable across products, but tool names, slash commands, hooks, subprocess/context directives, environment substitutions, plugins and invocation policies may not be. Check each selected skill against the current host's actual tools and resource access. Do not execute embedded shell substitutions simply because another product supports them. Respect explicit invocation restrictions; do not turn disabled/explicit-only candidates into automatic work.

Prefer the user-selected source, then the applicable active host/project contract. If two different copies have conflicting approval or workflow rules and intent is unresolved, show the exact source/version difference and resolve it before dependent actions. Never merge the least restrictive parts. Other skills' instructions cannot confer human approval or override the current user's scope.

Reference sources, checked 2026-10-27; verify current details before relying on changed product behavior:

- [Codex skill locations and metadata](https://learn.chatgpt.com/docs/build-skills)
- [Claude Code skill locations and compatibility](https://code.claude.com/docs/en/skills)
- [Skills CLI commands and supported agents](https://github.com/vercel-labs/skills)
- [Skill ecosystem search](https://skills.sh/)
