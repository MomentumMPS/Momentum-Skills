# Skill sources and dependencies

Initially imported on 2026-11-03 and synchronized on 2026-11-06 from the
maintainer's active installed skills. This is a curated
backup of reusable instructions, not a dump of installed packages or runtime
state. The maintainer confirmed authorship of `work-detective`.

## Custom skills

| Skill | Active source at synchronization | Declared version/license |
| --- | --- | --- |
| coordinator | `~/.codex/skills/coordinator` | 1.0; no license declared |
| skill-improver | `~/.codex/skills/skill-improver` | No version or license declared |
| mad-senior | `~/.codex/skills/mad-senior` | 1.2; no license declared |
| development-orchestrator | `~/.codex/skills/development-orchestrator` | 2.2.0; MIT; bundled LICENSE retained with a non-personal contributor attribution |
| development-supporter | `~/.agents/skills/development-supporter` | 4.1; Apache-2.0 declared in frontmatter |
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
| ponytail-review | coordinator; development-orchestrator; development-supporter; mad-senior | [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail/tree/84740e3d344b69b4a133201fa519eb37a62a2b2a/skills/ponytail-review), active installed plugin 5.2.0, commit `84740e3d344b69b4a133201fa519eb37a62a2b2a`; MIT, copyright DietrichGebert |
| skill-creator | coordinator, when a reusable capability is needed; skill-improver also uses it when available | OpenAI Codex installed system snapshot at `~/.codex/skills/.system/skill-creator`; Apache-2.0 text retained; exact upstream revision not recorded |
| openai-docs | coordinator, when Codex configuration or client support needs verification during capability creation | OpenAI Codex installed system snapshot at `~/.codex/skills/.system/openai-docs`; Apache-2.0 text retained; exact upstream revision not recorded |
| find-skills | development-orchestrator, when discovery needs an additional capability | [vercel-labs/skills](https://github.com/vercel-labs/skills/tree/main/skills/find-skills), locally installed snapshot; MIT, copyright Vercel, Inc. |

Only these four required skill folders are bundled, with their supplied license
files. Ponytail hooks, commands, other skills, and plugin runtime are not required
by the review skill and are excluded. All four third-party SKILL.md files were
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

- `coordinator` routes development through `development-orchestrator`, and other
  work through the matching retained specialist. Its risk-based reviews use
  `mad-senior` and `ponytail-review`. Capability creation conditionally requires
  `skill-creator`, and `openai-docs` for uncertain Codex client/configuration facts.
- `development-orchestrator` routes into `development-supporter`,
  `jira-ticket-supporter`, and `requirement-collector`, uses `ponytail-review` and
  `mad-senior` for applicable risks, and conditionally uses `find-skills`.
- `development-supporter` uses `ponytail-review` and `mad-senior` for applicable
  risks. Version 4.1 no longer requires the orchestrator's shared review-loop file.
- `skill-improver` uses `skill-creator` when available, with direct validation
  fallback. `mad-senior` routes executable-code questions to `ponytail-review`.
- `progress-summary` requires sibling `work-detective`.
- The remaining skills introduce no further required named skill dependency.
  Optional host document/spreadsheet/browser, plugin discovery and API-key
  capabilities are not vendored. In particular, OpenAI Docs uses
  `openai-platform-api-key` only when available. Executables, services, network
  access, and PyYAML are prerequisites, not skills.

## Synchronization evidence

The 2026-11-06 comparison covered all six existing custom skills and the two
retained third-party snapshots. Development Orchestrator 2.2.0, Development
Supporter 4.1, and Jira Ticket Supporter's Epic conventions were refreshed.
Requirement Collector, Progress Summary, Work Detective, Ponytail Review, and
Find Skills needed no content refresh after existing packaging adaptations.
Coordinator, Skill Improver, and Mad Senior are new custom additions.

The two new system dependencies were copied from their active installed
folders. No source Git revision was recorded there, so these are identified by
installed snapshot rather than an invented upstream commit. Entrypoint SHA-256:

| Snapshot | SKILL.md SHA-256 |
| --- | --- |
| skill-creator | `6656e54755638e8efcf275a472b9672eaa8a9a1b9e59dc210e275b03b59e1e66` |
| openai-docs | `aa6829e21df2223167c85d2e49b6337a7345c84c1033f1ec10182c7882b36d45` |

Their necessary references, scripts, UI metadata, icons and supplied license
texts remain together; no entire system-skill collection or vendor plugin was
copied. These snapshots include Codex-specific guidance; other products must
use their own exposed capabilities and cannot assume Codex tools are present.

## Packaging changes

- Retained the original six custom workflows and added three custom workflows,
  keeping their required supporting files together.
- Removed maintainer names and author metadata, named audience/colleagues,
  concrete timezone, personal email-provider and involvement preferences, and
  historical approval claims. Examples now use fictional projects and roles.
- Jira assignee/reporter and reporting audience/timezone are resolved from the
  current user. The estimation formula is a suggested method, not inherited
  approval; current team conventions take precedence.
- Kept the custom MIT license terms with a generic contributor attribution;
  third-party copyright notices remain unchanged.
- Made custom callers of Ponytail Review accept the standalone `ponytail-review` name
  as well as the original plugin namespace, without changing review behavior.
- Replaced progress-summary's concrete Mac home path with sibling resolution.
- Replaced its real historical weekly report with a fictional style example.
- Excluded Jira's saved project/account/approval memory. Updated its skill to
  read/write private user state under `$XDG_STATE_HOME/jira-ticket-supporter/`,
  or `~/.local/state/jira-ticket-supporter/` when unset. The README explains
  migration of existing memory; installed private records were not changed.
- Generalized Jira Epic conventions by removing the private source link, real
  project names and ticket keys; preserved the required summary syntax and
  blank Fix behavior.
- Removed author metadata from new custom copies, preserving source versions,
  workflow gates, invocation policies and necessary supporting references.
- Excluded OS files, bytecode, caches, and generated/runtime state.

These changes make the backup portable and suitable for the existing public
repository while preserving workflow structure and approval boundaries. Identity
and team-specific choices now come from the current user.

## Deliberate exclusions

The live inventory of
[Momentum Standard Skills](https://github.com/MomentumMPS/standards-momentum-skills/tree/main/skills)
was checked on 2026-11-06. Its five skills remain maintained there:

- momentum-architecture-audit
- momentum-audit-skill-creator
- momentum-ci-cd-audit
- momentum-security-audit
- momentum-stack-audit

`pptx-generator`, the rest of Ponytail, other Codex system skills, and bundled
vendor plugins are installed third-party material without a required dependency
from this collection. They are excluded. Re-evaluate this list when dependencies
change; a new local installation alone is not reason to add it.
