# CLAUDE

Derek's Plover stenography configuration. A **normal git repo** (not the bare `~/.cfg` repo) — use plain `git`, not the `dot` function. See `/home/derek/CLAUDE.md` for cross-platform dotfiles conventions (PowerShell-over-Bash, conventional commits, etc.).

## Two Configs: Linux vs Windows

**There are two `plover.cfg` files in this repo — do not confuse them.**

| File | Role | Serial port | Dictionary paths |
| --- | --- | --- | --- |
| `plover.cfg` (root) | **Linux** (live — this machine) | `/dev/serial/by-id/usb-StenoKeyboards_The_Uni-if02` | `plover/foo.md` (forward slashes, `plover/` prefix) |
| `plover/plover.cfg` | **Windows** (template, copied to `%APPDATA%\plover\` on Windows) | `COM36` | `foo.md` / `programs\bar.md` (backslashes, **no** `plover/` prefix) |

The Windows config lives inside `plover/` to mirror how Windows installs are laid out (config alongside dictionaries), so paths are relative without the prefix. Currently they are **out of sync** — `python_dictionary_testing_place.py` is disabled on Linux but enabled on Windows.

- `RepositoryScripts/SyncConfigFileDictionaries.ps1` — compares the dictionaries list between the two configs and reports sync state. Run this after editing either config.
- `plugins/` contains only `linux/` — Windows plugins are managed out-of-repo.

When editing dictionaries, **decide which config(s) the change applies to and keep them in sync** unless the change is platform-specific.

## Dictionary Formats

Three formats are in use, each loaded by a plugin. **Default to Markdown for new dictionaries.**

| Format | Plugin | Use |
| --- | --- | --- |
| **Markdown with embedded YAML** | `plover_markdown_dictionary` | Derek's favorite. Default for new dictionaries. |
| **Python** | `plover_python_dictionary` | Good for complex dictionary systems with logic (e.g. `emily-symbols.py`, `jeff-*.py`). |
| **JSON** | built-in | Plover's default — Derek **dislikes** it. A few exist for compatibility, but don't add new ones. |

### Markdown dictionaries are NOT `.yaml` files

The format is **YAML embedded inside `.md` files via ` ```yaml ` fenced code blocks** — there are no standalone `.yaml` dictionary files. The `plover_markdown_dictionary` plugin parses the fenced YAML blocks within the markdown. Prose/comments around the blocks are ignored by Plover but useful for humans. See `plover/personal.md` for the canonical pattern:

````markdown
# Some Dictionary

Optional prose comment.

```yaml
STROKE: "translation"   # inline comment
KPA: "{^}.{-|}"
```
````

## Dictionary Stack

`plover.cfg` defines the active dictionaries **in order** — earlier entries override later ones for the same stroke.

- `plover/main.json` (~147k lines) — **the bulk of English-language steno. Not Derek's work** (upstream Plover default). Do not edit unless explicitly asked.
- **Everything else under `plover/` is Derek's** unless listed as a submodule below.
- `plover/personal.md` sits near the top of the stack specifically to null out `main.json` defaults Derek wants to retrain himself out of.

## Submodules (Forks of Important Steno Repos)

All submodules are Derek's forks at `github.com/derekthecool/...`. The `jeff-*` ones are forked Python dictionaries worth studying before building similar systems.

| Path | Notes |
| --- | --- |
| `plover/jeff-numbers` | Forked Python number dictionary |
| `plover/jeff-phrasing` | Forked Python phrasing system |
| `plover/jeff-visual-stroke` | Forked visual stroke display |
| `plover-mouse` | Forked — **Derek intends to work on this but hasn't yet.** Treat as untouched upstream. |

## Critical Files

- `plover.cfg` — **Linux** Plover config + ordered dictionary stack
- `plover/plover.cfg` — **Windows** Plover config template
- `RepositoryScripts/SyncConfigFileDictionaries.ps1` — checks Linux/Windows dictionary lists match
- `plover/main.json` — upstream English dictionary (off-limits unless asked)
- `plover/personal.md` — Derek's overrides (canonical Markdown+YAML example)
- `README.md` — setup, plugin list, hardware (ZSA Moonlander), Arch build-from-source
- `Dereks_Plover_guide.md` — Derek's Plover reference (stroke syntax, key names, shortcut keys)

## Working with Dictionaries

- **New dictionary → Markdown with embedded YAML.** Study `plover/personal.md` for the pattern.
- Stroke syntax (`{^...}`, `{#...}`, `{&...}`, `{>}`, `{*}`, etc.) is documented in `Dereks_Plover_guide.md`.
- Dictionary order in `plover.cfg` is load-bearing — check it before adding/renaming dictionaries.
- If adding/renaming a dictionary, update **both** `plover.cfg` files (with correct path style for each) and run the sync script.
