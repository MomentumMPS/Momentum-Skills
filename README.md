# Skills

Reusable agent skills for coordination, development, requirements, ticket creation,
review, and work reporting. Maintained in
[pfonsecamoncada/Skills](https://github.com/pfonsecamoncada/Skills).
Skills maintained in
[Momentum Standard Skills](https://github.com/MomentumMPS/standards-momentum-skills)
belong there and are excluded here. Third-party skills are included only when
one of these custom skills depends on them.

## Collection

| Skill | Ownership | Purpose |
| --- | --- | --- |
| [coordinator](skills/coordinator) | Custom | Coordinate the overall outcome across specialist skills and bounded agents. |
| [skill-improver](skills/skill-improver) | Custom | Review and improve skill intent, strategy, and instructions. |
| [mad-senior](skills/mad-senior) | Custom | Review consequential non-code decisions and evidence. |
| [development-orchestrator](skills/development-orchestrator) | Custom | Coordinate skills, reviews, approvals, and delivery. |
| [development-supporter](skills/development-supporter) | Custom | Resolve Jira work through code, branch setup, or a no-code outcome. |
| [jira-ticket-supporter](skills/jira-ticket-supporter) | Custom | Draft and create Jira tickets with reusable templates and verified context. |
| [requirement-collector](skills/requirement-collector) | Custom | Consolidate requirements and prepare approved ticket drafts. |
| [progress-summary](skills/progress-summary) | Custom | Write a weekly spoken leadership update from work evidence. |
| [slack-message-drafter](skills/slack-message-drafter) | Custom | Draft Slack messages using the current user’s evidenced voice. |
| [work-detective](skills/work-detective) | Custom | Reconstruct work across connected sources with supporting evidence. |
| [ponytail](skills/ponytail) | Third-party dependency | Apply the smallest complete implementation in development workflows. |
| [ponytail-review](skills/ponytail-review) | Third-party dependency | Review proposals and results for the development workflows. |
| [find-skills](skills/find-skills) | Third-party dependency | Discover missing capabilities for development-orchestrator. |
| [skill-creator](skills/skill-creator) | Third-party dependency | Author and validate capabilities when Coordinator needs them. |
| [openai-docs](skills/openai-docs) | Third-party dependency | Verify Codex configuration and client guidance for capability creation. |

Everything lives directly under `skills/<skill-name>/`. Supporting files stay
with their skill. There are no product-specific copies or category directories.
[SOURCES.md](SOURCES.md) records origins, dependencies, exclusions, and packaging
changes. [AGENTS.md](AGENTS.md) defines how to maintain this repository.

## Install globally

Here, **global means user-level: available across all local projects for your
operating-system account**. Never install this collection into an individual
project. Installation does not require administrator access or `sudo`.

The installation uses these documented locations:

| Product | User-level location used here | Documentation |
| --- | --- | --- |
| Codex | `~/.agents/skills/` | [OpenAI skill locations](https://learn.chatgpt.com/docs/build-skills) |
| Claude Code | `~/.claude/skills/` | [Claude Code personal skills](https://code.claude.com/docs/en/skills) |
| Cursor | `~/.agents/skills/`, shared with Codex | [Cursor skill locations](https://cursor.com/help/customization/skills) |

### macOS and Linux

Requires Git and Python 3. Keep the clone in a permanent location under your
home directory. For example:

```sh
mkdir -p "$HOME/.local/share"
git clone https://github.com/pfonsecamoncada/Skills.git "$HOME/.local/share/agent-skills"
cd "$HOME/.local/share/agent-skills"
python3 install.py --dry-run
python3 install.py
```

If you already have a clone, run the last two commands from that clone instead.
The installer links each complete skill folder into the two user-level roots.
Codex and Cursor share one root; Claude Code uses the other. Dependencies are
included automatically. Links point to the clone, so keep it in place.

Existing links to this clone are accepted on reruns. An existing directory,
different link, or broken link with the same name stops installation before any
links are created. Compare its contents with this repository and preserve local
edits before moving it to a backup location **outside all skill discovery
folders**. Do not use force-overwrite commands. Retry after resolving the
reported conflicts. A later filesystem/permission failure can leave some links
installed; correct that error and rerun safely.

When migrating an older `jira-ticket-supporter`, keep its
`references/project-memory.json` private. Move that file to
`~/.local/state/jira-ticket-supporter/project-memory.json`, or the equivalent
location under your configured `XDG_STATE_HOME`, before retiring the old skill.
Do not overwrite existing state; reconcile both sets of entries if necessary.

Check for older duplicate installations in `~/.codex/skills/`,
`~/.cursor/skills/`, and enabled plugins. The installer does not remove them.
Keep one active source for each skill after comparing any local differences;
duplicate copies can produce duplicate or conflicting skill choices.

### Windows

For tools running inside WSL, use the Linux instructions inside that WSL user
account. For native Windows tools, clone into a permanent directory under your
Windows user profile and run:

```powershell
py -3 install.py --dry-run
py -3 install.py
```

Native Windows symlinks require suitable permissions (commonly Developer Mode).
If symlinks are unavailable, copy each complete `skills/<skill-name>` directory
into `%USERPROFILE%\.agents\skills\` and `%USERPROFILE%\.claude\skills\` after
checking for conflicts. Keep all fifteen folders together in each location so
relative dependency references resolve. Copies must be updated manually.

### Verify and use

Start a fresh session in each product, open an unrelated project, and ask it to
list the available skills. Confirm the ten custom skills and five dependencies
appear. For example: "Use requirement-collector to organize these requirements."
Codex also supports `$skill-name`; Claude Code and Cursor support `/skill-name`.

The installer supplies instructions and supporting files, not service access.
Jira workflows require authenticated `acli`; repository delivery requires Git
and `gh`; discovery through `find-skills` uses Node.js/npm. Work research needs
the relevant connectors or permitted browser/desktop tools. Check the selected
skill's prerequisites and use the capabilities exposed by the current product.
Skill validation uses Python 3 with PyYAML; the OpenAI Docs helpers use Node.js
and network access. Install these only when their selected workflow needs them.
Installing a skill does not install connectors or authorize external writes.

When a required tool is missing, ask your assistant to help install it from its
official source and verify it before continuing that workflow. Install optional
tools only when needed. This repository bundles the five required third-party
skill folders, not their entire upstream packages, command-line tools, or
binaries. Their licenses and sources are recorded in SOURCES.md.

The skills resolve identity, assignee, audience, timezone, and service choices
from the current user's context. No maintainer account, personal reporting
preferences, or private project memory is bundled. Shared skill files do not
make every product's tools interchangeable.
`agents/openai.yaml` is optional Codex metadata; the portable entrypoint is
`SKILL.md`.

User-level files apply to local sessions. They are not automatically installed
into remote machines, cloud agents, or other operating-system accounts.

## Update, back up, and remove

From the permanent clone, run `git pull --ff-only`, review the changes, and run
`python3 install.py` again to link newly added skills. Existing links immediately
see updated files. Preserve local edits before pulling; do not reset them away.
If a skill is removed from the repository, remove its obsolete user-level links
after checking their targets.

For installations linked to this clone, changes through an installed symlink
also change the repository. When backing up separately maintained installed
skills, compare their active sources and apply privacy and portability changes
only to repository copies. Review `git diff` before committing and pushing backups. Do not copy entire installed-skill or plugin-cache directories
into the repository.

To uninstall, remove only the per-skill symlinks that point into this clone from
`~/.agents/skills/` and `~/.claude/skills/`. Keep unrelated skills and private
runtime state. Remove the clone only after its links are gone and any edits are
backed up. For copy-based installs, compare and back up local edits before
removing those specific copied folders.

## Maintenance checks

```sh
python3 -m unittest -v test_install.py
git diff --check
```

The installer tests use temporary directories and do not touch installed
skills. Also check each changed skill's frontmatter, local references, dependency
closure, and provenance. Keep runtime memory, credentials, work reports, and
machine-specific absolute paths out of backups. Existing per-skill licenses are
preserved; see [SOURCES.md](SOURCES.md) for license scope.
