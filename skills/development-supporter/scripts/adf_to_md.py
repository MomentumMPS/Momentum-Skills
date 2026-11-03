#!/usr/bin/env python3
"""Convert Jira Atlassian Document Format (ADF) into readable Markdown.

Usage:
  acli jira workitem view ABC-123 --fields "*all" --json \
    | python3 scripts/adf_to_md.py --field description

  acli jira workitem view ABC-123 --fields "*all" --json \
    | python3 scripts/adf_to_md.py --field customfield_10045

  echo '<adf json>' | python3 scripts/adf_to_md.py --raw

Plain string fields are printed as they are. Missing or empty fields print
nothing and exit 0, so callers can test for empty output.
"""
import argparse
import json
import sys


def inline(nodes):
    out = []
    for n in nodes or []:
        t = n.get("type")
        if t == "text":
            text = n.get("text", "")
            marks = {m.get("type") for m in n.get("marks", [])}
            link = next((m for m in n.get("marks", []) if m.get("type") == "link"), None)
            if "code" in marks:
                text = "`" + text + "`"
            if "strong" in marks:
                text = "**" + text + "**"
            if "em" in marks:
                text = "*" + text + "*"
            if link:
                text = "[" + text + "](" + link.get("attrs", {}).get("href", "") + ")"
            out.append(text)
        elif t == "hardBreak":
            out.append("\n")
        elif t == "mention":
            out.append(n.get("attrs", {}).get("text", "@user"))
        elif t == "emoji":
            out.append(n.get("attrs", {}).get("shortName", ""))
        elif t in ("inlineCard", "blockCard", "embedCard"):
            out.append(n.get("attrs", {}).get("url", ""))
        elif t == "status":
            out.append("[" + n.get("attrs", {}).get("text", "") + "]")
        elif t == "date":
            out.append(str(n.get("attrs", {}).get("timestamp", "")))
        else:
            out.append(inline(n.get("content")))
    return "".join(out)


def block(n, depth=0):
    t = n.get("type")
    c = n.get("content", [])
    pad = "  " * depth
    if t == "doc":
        return "\n\n".join(filter(None, (block(x, depth) for x in c)))
    if t == "paragraph":
        return inline(c)
    if t == "heading":
        return "#" * n.get("attrs", {}).get("level", 2) + " " + inline(c)
    if t in ("bulletList", "orderedList"):
        lines = []
        for i, item in enumerate(c, 1):
            marker = (str(i) + ".") if t == "orderedList" else "-"
            parts = [block(x, depth + 1) for x in item.get("content", [])]
            first, rest = (parts[0] if parts else ""), parts[1:]
            lines.append(pad + marker + " " + first.strip())
            lines.extend(p for p in rest if p)
        return "\n".join(lines)
    if t == "taskList":
        return "\n".join(
            pad + ("- [x] " if i.get("attrs", {}).get("state") == "DONE" else "- [ ] ")
            + inline(i.get("content")) for i in c)
    if t == "codeBlock":
        lang = n.get("attrs", {}).get("language", "") or ""
        return "```" + lang + "\n" + inline(c) + "\n```"
    if t == "blockquote":
        return "\n".join("> " + line for line in
                         "\n\n".join(block(x) for x in c).splitlines())
    if t == "panel":
        kind = n.get("attrs", {}).get("panelType", "info").upper()
        return "[" + kind + "] " + "\n".join(block(x) for x in c)
    if t == "rule":
        return "---"
    if t == "table":
        rows = []
        for r_i, row in enumerate(c):
            cells = [" ".join(block(x) for x in cell.get("content", [])).replace("\n", " ")
                     for cell in row.get("content", [])]
            rows.append("| " + " | ".join(cells) + " |")
            if r_i == 0:
                rows.append("|" + "---|" * len(cells))
        return "\n".join(rows)
    if t in ("mediaSingle", "mediaGroup", "media"):
        ids = [m.get("attrs", {}).get("id") or m.get("attrs", {}).get("alt", "")
               for m in ([n] if t == "media" else c)]
        return "[attachment: " + ", ".join(filter(None, ids)) + "]"
    if t in ("expand", "nestedExpand"):
        title = n.get("attrs", {}).get("title", "")
        return "**" + title + "**\n" + "\n\n".join(block(x, depth) for x in c)
    return inline(c) if c else inline([n])


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--field", default="description")
    ap.add_argument("--raw", action="store_true", help="stdin is an ADF node")
    args = ap.parse_args()
    try:
        data = json.load(sys.stdin)
    except json.JSONDecodeError as e:
        sys.exit("adf_to_md: stdin is not valid JSON: " + str(e))
    if not args.raw:
        if isinstance(data, list):
            data = data[0] if data else {}
        data = (data.get("fields") or {}).get(args.field)
    if data in (None, "", {}):
        return
    if isinstance(data, str):
        print(data)
    elif isinstance(data, (int, float)):
        print(data)
    elif isinstance(data, dict) and data.get("type"):
        print(block(data).strip())
    else:
        print(json.dumps(data, indent=2))


if __name__ == "__main__":
    main()
