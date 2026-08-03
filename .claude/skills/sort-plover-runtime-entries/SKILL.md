---
name: sort-plover-runtime-entries
description: Sort runtime-captured entries from "Added by Plover" markdown sections into their correct curated Plover dictionary (personal/powershell/programming/work/church). Triggers on "sort plover", "organize added entries", "tidy runtime dictionary", "triage plover added", "plover runtime entries".
allowed-tools: Read,Grep,Edit,AskUserQuestion
---

# Sort Plover Runtime Entries

Triage entries that Plover captured at runtime into the correct curated markdown dictionary. Runtime entries live under `## Added by Plover` headings and are typically bare `STROKE: translation` lines (no inline comments). Curated entries elsewhere in each file often have `# explanation` comments and use richer Plover syntax.

## When to Use

Invoke when the user wants to sort, organize, tidy, triage, or distribute entries that Plover auto-captured into `## Added by Plover` sections. Trigger phrases: "sort plover", "organize added entries", "tidy runtime dictionary", "triage plover added", "plover runtime entries".

## Workflow

1. **Locate runtime sections.** `Grep` for `^## Added by Plover` across these five files (paths relative to repo root):
   - `plover/personal.md`
   - `plover/powershell.md`
   - `plover/programming.md` (expect TWO matches — process both as one logical queue)
   - `plover/work.md`
   - `plover/churchofjesuschristoflatterdaysaints.md`

   For each match, `Read` from the heading line through the next closing ` ``` ` fence and capture every `STROKE: translation` line in between.

2. **Filter to runtime-captured entries only.** A candidate line matches `^[A-Z0-9*/+\-']+\s*:\s*.+`. Skip:
   - Blank lines and `#`-prefixed comments
   - Multi-line YAML values (folded `>` or block arrays) — these are hand-authored, not runtime-captured
   - Anything outside an `Added by Plover` block

3. **If zero candidates across all five files:** print `No runtime entries to sort — all tidy.` and stop.

4. **Classify each entry** using the rules in **Categorization rules** below. Tag each entry as either:
   - `high-confidence → <dest-file>`
   - `low-confidence` (no rule matched)

5. **Dedup check** for each high-confidence entry. `Grep` the destination file for `^<STROKE>:` (escape regex special chars in the stroke). If a match exists in any yaml block that is NOT an `Added by Plover` block, reclassify the entry as a `dedup-conflict`.

6. **Batch ask.** Collect every `low-confidence` and `dedup-conflict` entry. If the collection is non-empty, issue **one** `AskUserQuestion` call with one sub-question per entry. Each sub-question's options are the five destination files plus "Skip this entry". Use the entry's stroke and translation as the question text and a brief reason ("no rule matched" / "exists at <file>:<line>") in the header. Stop and wait for the user's answers before continuing.

7. **Apply moves.** For each entry with a resolved destination (either high-confidence, or user-answered):
   - `Read` the destination yaml block chosen per **Insertion point** below.
   - `Edit` the destination: insert the entry on a new line immediately before the block's closing ` ``` ` fence. Match surrounding style — if neighboring entries have inline `# comment`s, append ` # sorted from Added by Plover` to the inserted line; if neighbors are bare, insert bare.
   - `Edit` the source: delete the entry's line from its `Added by Plover` block. If this leaves the block's yaml fence empty, leave the heading and empty fence in place — Plover will refill it on next capture.

8. **Do not commit.** Do not run any `git` command. Do not stage. The user explicitly wants changes left unstaged for review.

9. **Print summary.** Report:
   - A per-source-file table: `source.md → destination.md (count)` for each destination, including intra-file moves (e.g. `programming.md → programming.md/themed block`).
   - Skipped duplicates with `file:line` citations.
   - Any user-answered overrides (entries where the user picked a different file than the heuristic suggested, or chose "skip").
   - A final line: `Changes left unstaged. Review with git diff.`

## Categorization Rules

Priority-ordered. Apply to the **lowercased translation text**. If translation is empty, classify on the stroke alone. First matching rule wins; if no rule matches, mark `low-confidence`.

1. **`plover/powershell.md`** — translation matches `^(get|set|new|remove|invoke|select|start|stop|import|export|write|out|where|foreach|test|convertto|convertfrom|measure|sort|group|compare|update|add)-[a-z]`, OR contains any of: `::`, `@(`, `.GetType()`, `.ToString()`, `ExpandProperty`, `ValueFromPipeline`, `pwsh`, `psake`. Also matches known cmdlet aliases: `gci`, `gc`, `select-string`, `foreach-object`, `where-object`.

2. **`plover/churchofjesuschristoflatterdaysaints.md`** — translation contains any of: `mormon`, `book of mormon`, `nephi`, `latter-day`, `latter day`, `ward`, `stake`, `bishop`, `scripture`, `doctrine`, `covenants`, `prophet`, `general conference`, or matches the phrase `book of`.

3. **`plover/work.md`** — translation contains any of: `verizon`, `twilio`, `becklar`, `freeus`, `safetylink`. (`alarm`, `backend`, `frontend` only count when co-occurring with one of the employer tokens above.)

4. **`plover/programming.md`** — translation matches:
   - A file extension: `.py`, `.yaml`, `.toml`, `.json`, `.sdk`, `.com` (but `.com` only if not preceded by a person's name — if unclear, treat as low-confidence)
   - A dev-tool or language name: `docker`, `nginx`, `daemon`, `kotlin`, `regex`, `gradle`, `pwd`, `sdk`, `vpn`, `utc`, `localhost`, `127.0.0.1`, `pacman`, `az`, `proxy`, `firefox`, `binary`, `obsidian`, `shutdown`, `extern`, `remove`, `usr`, `yaml`, `curl`, `nginx`, `mpv`, `r2`, `rabin2`, `nix-shell`, `nix-build`, `flutter`
   - A Plover-format attachment prefix: `{^}usr`, `{^}yaml`, or similar `{^}<token>` patterns where the token is a dev path/component
   - A URL or curl template (`https://`, `curl -sL`, etc.)

5. **Otherwise:** `low-confidence` → ask the user. Do NOT silently default to `personal.md`.

## Insertion Point

For each destination file, choose the target yaml block:

- **`personal.md`** → `## General Words` (the only curated block)
- **`programming.md`** → match by theme to a heading such as `## Common To Most Languages`, `## Nix and NixOS`, `## Flutter`, `## Quick Curl Installs`, `## Networking`, `## Nix and NixOS`. If no heading is a clear thematic fit, fall back to the **last non-`Added by Plover` yaml block** in the file.
- **`powershell.md`** → if headings bucket by cmdlet verb family, pick the matching bucket; else the last non-runtime block.
- **`work.md`**, **`churchofjesuschristoflatterdaysaints.md`** → single curated block each; use it.

Never insert into an `Added by Plover` block.

## Edge Cases

- **`programming.md` has two `## Added by Plover` sections** (one mid-file at line ~920, one truly final at line ~955). Process both as one queue; attribute all moves to `programming.md` in the summary. Do not warn — this is the known repo state.
- **Empty runtime block after moves:** leave the heading and empty yaml fence in place. Plover will refill on next capture.
- **Exact duplicate of an existing curated entry:** reclassify as `dedup-conflict` and ask the user. Offer: skip / overwrite / pick a different destination.
- **Entry translation contains Plover syntax** (`{^}`, `{-|}`, `{#...}`, `{MODE:...}`): preserve verbatim on insert. Classification still runs on the readable portion of the translation.
- **Multi-line YAML value inside a runtime block:** skip with a warning in the summary. These are not runtime-captured and should not be moved.

## Reference

- Curated markdown+YAML dictionary pattern: see `plover/personal.md` for the canonical format (prose heading + ` ```yaml ` fenced block + optional inline `# comment`s).
- Parent repo conventions: see `/home/derek/.config/plover/CLAUDE.md` for the Linux/Windows dual-config split, dictionary format preferences, and submodule layout.
