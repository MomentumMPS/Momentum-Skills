# Skill sources and dependencies

Imported on 2026-11-03 from the maintainer's active installed skills. This is a curated
backup of reusable instructions, not a dump of installed packages or runtime
state. The maintainer confirmed authorship of `work-detective`.

## Custom skills

| Skill | Source at import | Declared version/license |
| --- | --- | --- |
| development-orchestrator | `~/.codex/skills/development-orchestrator` | MIT; bundled LICENSE retained with a non-personal contributor attribution |
| development-supporter | `~/.agents/skills/development-supporter` | 3.9; Apache-2.0 declared in frontmatter |
| jira-ticket-supporter | `~/.agents/skills/jira-ticket-supporter` | No version or license declared |
| requirement-collector | `~/.agents/skills/requirement-collector` | No version or license declared |
| progress-summary | `~/.agents/skills/progress-summary` | No version or license declared |
| work-detective | `~/.agents/skills/work-detective` | No version or license declared |

Codex links for the shared skills resolve to `~/.agents/skills`. Older Claude
copies differed for development-supporter, jira-ticket-supporter, and
requirement-collector. The active Codex/shared sources above were selected;
those older copies and all installed originals were left untouched.

## Required third-party skills

| Skill | Required by | Source and license |
| --- | --- | --- |
| ponytail-review | development-orchestrator; development-supporter | [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail/tree/84740e3d344b69b4a133201fa519eb37a62a2b2a/skills/ponytail-review), active installed plugin 5.2.0, commit `84740e3d344b69b4a133201fa519eb37a62a2b2a`; MIT, copyright DietrichGebert |
| find-skills | development-orchestrator, when discovery needs an additional capability | [vercel-labs/skills](https://github.com/vercel-labs/skills/tree/main/skills/find-skills), locally installed snapshot; MIT, copyright Vercel, Inc. |

Only these required skill folders are bundled, with their upstream LICENSE
files. Ponytail hooks, commands, other skills, and plugin runtime are not required
by the review skill and are excluded. The two third-party SKILL.md files were
copied without edits.

The local Skills CLI lock records `find-skills` from `vercel-labs/skills`, path
`skills/find-skills/SKILL.md`, installed/updated 2026-10-16, with folder hash
`76a98a285cb0434f3d39e1a873823556330e398b`. This is a folder hash, **not** a Git
commit. The installed SKILL.md SHA-256 is
`c00eeea0e13e74fe4a9d84ba0a8542205a1b736d65f13134fe1a6647eb14976f`. Its exact upstream commit was not recorded. The upstream
MIT license was retrieved on 2026-11-03; upstream HEAD at retrieval was
`7a5e920bead4b1039a6d6df5d7e1163b7b09423a`, not an asserted skill snapshot revision.

No repository-wide license is imposed. Each supplied license applies to its
own material; absence of a license is not a new redistribution grant.

## Dependency closure

- `development-orchestrator` routes into `development-supporter`,
  `jira-ticket-supporter`, and `requirement-collector`, requires `ponytail-review`,
  and conditionally uses `find-skills` for capability discovery.
- `development-supporter` requires `ponytail-review` and the shared
  `development-orchestrator/references/review-loop.md` resource. This is a shared
  resource dependency, not permission to restart orchestration recursively.
- `progress-summary` requires sibling `work-detective`.
- `jira-ticket-supporter`, `requirement-collector`, `work-detective`,
  `ponytail-review`, and `find-skills` have no further mandatory named skill
  dependencies. Host document/spreadsheet/browser guidance is used when
  available and appropriate; those optional capabilities are not vendored.

## Packaging changes

- Retained the six custom workflows and their required supporting files.
- Removed maintainer names and author metadata, named audience/colleagues,
  concrete timezone, personal email-provider and involvement preferences, and
  historical approval claims. Examples now use fictional projects and roles.
- Jira assignee/reporter and reporting audience/timezone are resolved from the
  current user. The estimation formula is a suggested method, not inherited
  approval; current team conventions take precedence.
- Kept the custom MIT license terms with a generic contributor attribution;
  third-party copyright notices remain unchanged.
- Made Ponytail Review references accept the standalone `ponytail-review` name
  as well as the original plugin namespace, without changing review behavior.
- Replaced progress-summary's concrete Mac home path with sibling resolution.
- Replaced its real historical weekly report with a fictional style example.
- Excluded Jira's saved project/account/approval memory. Updated its skill to
  read/write private user state under `$XDG_STATE_HOME/jira-ticket-supporter/`,
  or `~/.local/state/jira-ticket-supporter/` when unset. The README explains
  migration of existing memory; installed private records were not changed.
- Excluded OS files, bytecode, caches, and generated/runtime state.

These changes make the backup portable and suitable for the existing public
repository while preserving workflow structure and approval boundaries. Identity
and team-specific choices now come from the current user.

## Deliberate exclusions

The live inventory of
[Momentum Standard Skills](https://github.com/MomentumMPS/standards-momentum-skills/tree/main/skills)
was checked on 2026-11-03. Its four skills remain maintained there:

- momentum-architecture-audit
- momentum-audit-skill-creator
- momentum-ci-cd-audit
- momentum-stack-audit

`pptx-generator`, the rest of Ponytail, Codex system skills, and bundled vendor
plugins are installed third-party material without a required dependency from
this collection. They are excluded. Re-evaluate this list when dependencies
change; a new local installation alone is not reason to add it.
