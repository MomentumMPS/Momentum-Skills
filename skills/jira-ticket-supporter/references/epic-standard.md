# Epic summary standard

Apply this standard whenever drafting or creating a new Epic. It overrides only the generic app/project summary format; retain the skill's description template, field defaults, and authorization requirements.

## Required format

`EPC - CATEGORY - Description`

- `EPC` is the fixed prefix marking the issue as an Epic.
- `CATEGORY` is a short uppercase code for the domain or platform area.
- `Description` is a plain-language name of the Epic's scope.
- Use a space, hyphen, and space between the three parts. The brackets in the notation `EPC - [CATEGORY] - [Description]` mark placeholders and are not literal title characters. Do not prepend the app/project title before `EPC`; include the app name in the description when it helps identify scope.

Choose the category from the user's instruction, relevant established Epic conventions, or clear domain/platform context. The examples below are not an exhaustive list of allowed categories. If context does not support a category, resolve it with the user before creation rather than inventing a code or using a placeholder.

Before creation, check the fixed prefix, uppercase category, separators, and plain-language scope. After creation, verify the saved summary matches the prepared title and this standard through the normal acli read-back.

## Fictional examples

These examples illustrate the format; they are not existing work records or default parents.

| Example summary | Meaning |
| --- | --- |
| `EPC - SUP - Operational Reporting Requests` | Support and reporting scope |
| `EPC - APP - Team Resource Portal` | Application scope |
| `EPC - ARCH - Data Platform Migration` | Architecture scope |

Apply the current user's or team's explicit convention when it differs from this reusable default. This creation rule does not authorize renaming existing tickets.
