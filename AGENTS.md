# Repository instructions

## Scope and ownership

This repository backs up the maintainer's custom skills that are not maintained
in `MomentumMPS/standards-momentum-skills`. Compare that repository's actual
inventory before adding or moving a skill; do not classify solely by its name.
Do not duplicate its four audit/audit-authoring skills here.

Include a third-party skill only when a retained custom skill requires it,
including a conditional workflow dependency. Record the consuming skill,
upstream source, known revision, license, and local modifications in SOURCES.md.
Follow dependencies transitively. Generic optional host capabilities (browser,
document, or spreadsheet support) do not justify copying entire vendor plugins.
Do not treat local installation as evidence of the maintainer's authorship.

External executables and services are prerequisites, not vendored skills.
Document required tools (such as Git, gh, acli, Python, and Node.js) and guide
their installation only when the selected workflow needs them. Do not bundle
binaries, package caches, credentials, or an entire plugin for one skill.
Suggest optional capabilities when relevant rather than installing them all.

## Layout

- Keep one flat `skills/<skill-name>/` collection for custom skills and required
  third-party dependencies. Mark ownership in the README and SOURCES tables.
- Keep each SKILL.md and its necessary references, scripts, assets, and optional
  agent metadata together. Preserve folder names used by dependency links.
- Keep repository documentation and the installer at the root. Add directories
  only for a real resource need; no per-product copies, category trees, generated
  bundles, or duplicated installation guides.
- Back up real files, not links into one machine's installed skill directories.

## Installation and portability

Document and support global user-level installation only, across projects.
Use home-relative or resolved paths, never one person's concrete home path.
The installer uses `~/.agents/skills` for Codex/Cursor and `~/.claude/skills` for
Claude Code. Verify official documentation before changing product discovery
guidance. Do not silently overwrite or remove existing installations.

Keep required skills as siblings. Resolve supporting resources relative to the
skill's real directory. Allow standalone dependency names as well as a plugin
namespace when applicable. Do not assume a tool, connector, account, or plugin
exists in every agent product. Preserve invocation policies and workflow gates.

## Backups and changes

Read installed skills as source artifacts when backing them up; copying a
workflow does not activate it or authorize its Jira, messaging, or deployment
actions. Prefer the active, user-selected version when copies differ. Preserve
installed originals unless the user requests installation or migration.

Publish reusable workflows without the maintainer's personal information or
private defaults. Resolve identity, accounts, audience, timezone, and team
preferences from the current user's context. Keep private runtime memory, account
identifiers, credentials, approval records, and real work evidence out of this
public repository. Use fictional examples and user-state directories outside
the checkout for mutable memory. Apply sanitization only to repository copies;
never remove personal data from the maintainer's installed originals. Record
packaging and portability changes in SOURCES.md.

Do not apply a blanket license to third-party or unlicensed skills. Preserve
existing notices and obtain actual provenance rather than inventing authorship,
versions, or permission. Add only dependencies required by the retained skills.

Before delivery, verify the skill inventory, dependency closure, frontmatter,
local references, absence of private state, and `git diff --check`. Run installer
tests when installation behavior changes. Test in temporary directories, never
by replacing the user's installed skills. Report actual validation limits.

Keep README.md and SOURCES.md aligned with the final collection. Publish to the
personal repository when authorized; syncing the Momentum fork is a separate
action and is not automatic.

## Conversation titles

When title tools are available, apply this title convention without asking:

- One identified work ticket: `KEY-123: Ticket summary`, using its real summary.
- Multiple identified work tickets: `[2 TICKETS][KEY-123 & KEY-456]: Combined summary`,
  adjusting count and keys as needed.
- Without a specific ticket work item: preserve the descriptive title and prefix
  `[NO-TICKET] ` exactly once. General discovery, triage, QA, audits, deployment,
  and administration may remain NO-TICKET despite incidental ticket mentions.
- When the work takes on a specific ticket, replace the generic title. Preserve
  titles already following the convention. Rename only the current chat.

## Jira authentication

Follow the current host's sandbox and approval rules. If a sandbox prevents
access to the authenticated CLI session or network, retry in an authorized
execution context before asking for login. All Jira write authorization
requirements still apply.
