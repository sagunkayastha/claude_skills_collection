---
name: obsidian-sync
description: Use when interacting with Obsidian vaults from the terminal — creating, reading, searching, syncing notes, managing tasks, daily notes, plugins, or any vault operation. Supports official Obsidian CLI (v1.12+, local) and obsidian-headless (ob, remote/HPC). Triggers on "obsidian", "vault", "sync to obsidian", "daily note", "push to vault", or Obsidian CLI commands.
---

# Obsidian CLI

Two CLI tools for Obsidian, each with different strengths:

| | Official CLI (`obsidian`) | obsidian-headless (`ob`) |
|---|---|---|
| **How it works** | Talks to running Obsidian app | Standalone, no app needed |
| **Best for** | Local vault operations, search, tasks, plugins | Remote/HPC sync, headless servers, CI/CD |
| **Requires** | Obsidian 1.12+ running | Node.js + `npm install -g obsidian-headless` |
| **Sync** | Uses app's built-in Sync | Direct API to Obsidian Sync servers |

**Decision:** Use official CLI when Obsidian is running locally. Use `ob` when on a remote server (NERSC, SSH) or when Obsidian app isn't available.

---

# Part 1: Official Obsidian CLI (v1.12+)

## Prerequisites

- Obsidian 1.12+ with CLI enabled (Settings > General > Command line interface)
- Obsidian must be running (CLI talks to the app)
- Windows binary: `C:\Users\sgnka\AppData\Local\Obsidian\Obsidian.com`

**Shell alias (use in all commands):**
```bash
OB="/c/Users/sgnka/AppData/Local/Obsidian/Obsidian.com"
```

## Known Vaults

| Name | Path |
|------|------|
| Sync_vault | `C:\Users\sgnka\OneDrive - University Of Houston\Documents\Sync_vault` |
| claude_vault | `E:\Obsidian_vaults\claude_vault\claude_vault` |
| iCloud~md~obsidian | `C:\Users\sgnka\iCloudDrive\iCloud~md~obsidian` |

Target a vault: `$OB <command> vault=claude_vault`

## Quick Reference

### File Operations

```bash
# Create a note
$OB create name="My Note" content="# Title\nBody text" vault=claude_vault

# Create in subfolder
$OB create path="folder/note.md" content="content here"

# Create from template
$OB create name="Meeting" template="meeting-template"

# Read a note
$OB read file="My Note"
$OB read path="folder/note.md"

# Append/prepend to a note
$OB append file="My Note" content="\n## New Section\nText here"
$OB prepend file="My Note" content="Prepended line"

# Move/rename
$OB move file="Old Name" to="new-folder/Old Name.md"
$OB rename file="Old Name" name="New Name"

# Delete (to trash)
$OB delete file="My Note"
$OB delete file="My Note" permanent  # skip trash
```

### Search

```bash
$OB search query="search terms" vault=claude_vault
$OB search query="exact phrase" limit=10
$OB search:context query="search terms" limit=5  # with matching lines
$OB search query="topic" path="Projects"          # in specific folder
```

### Daily Notes

```bash
$OB daily                                    # Open today's daily note
$OB daily:read                               # Read today's daily note
$OB daily:append content="- Task from CLI"   # Append to daily note
$OB daily:prepend content="## Morning"       # Prepend to daily note
$OB daily:path                               # Get daily note file path
```

### Tasks

```bash
$OB tasks                        # All tasks
$OB tasks todo                   # Incomplete only
$OB tasks done                   # Completed only
$OB tasks file="Project Plan"    # Tasks in specific file
$OB tasks daily                  # Tasks in today's daily note
$OB tasks verbose                # Group by file with line numbers

# Toggle/update a task
$OB task path="notes/todo.md" line=5 toggle
$OB task path="notes/todo.md" line=5 done
```

### Properties (Frontmatter)

```bash
$OB property:read name="status" file="My Note"
$OB property:set name="status" value="in-progress" file="My Note"
$OB property:set name="tags" value="project,active" type=list file="My Note"
$OB property:remove name="draft" file="My Note"
$OB properties counts sort=count
```

### Vault Info

```bash
$OB vault                        # Vault info (name, path, size)
$OB vaults verbose               # List all vaults with paths
$OB files folder="Projects"      # Files in folder
$OB files ext=md total           # Count markdown files
$OB folders                      # List all folders
$OB tags counts sort=count       # List tags with counts
```

### Links & Graph

```bash
$OB links file="My Note"        # Outgoing links
$OB backlinks file="My Note"    # Incoming links
$OB orphans                     # Files with no incoming links
$OB deadends                    # Files with no outgoing links
$OB unresolved                  # Broken links
```

### Sync (via app)

```bash
$OB sync:status                  # Show sync status
$OB sync on                      # Resume sync
$OB sync off                     # Pause sync
$OB sync:history file="My Note"  # Version history
$OB sync:read file="My Note" version=1
$OB sync:restore file="My Note" version=3
$OB sync:deleted                 # List deleted files in sync
```

### Plugins & Themes

```bash
$OB plugins                               # All installed
$OB plugins:enabled filter=community versions
$OB plugin:install id="dataview" enable
$OB plugin:disable id="dataview"
$OB plugin:enable id="dataview"
$OB themes
$OB theme:install name="Minimal" enable
$OB theme:set name="Minimal"
```

### Templates & Bookmarks

```bash
$OB templates
$OB template:read name="daily" resolve title="Today"
$OB bookmarks
$OB bookmark file="Important.md" title="Key Reference"
```

### History (File Recovery)

```bash
$OB history file="My Note"
$OB history:read file="My Note" version=1
$OB history:restore file="My Note" version=2
```

### Developer Commands

```bash
$OB eval code="app.vault.getFiles().length"
$OB dev:screenshot path="screenshot.png"
$OB dev:console
$OB dev:errors
$OB commands
$OB command id="app:reload"
```

## Workflow: Push Local Files to Vault

```bash
OB="/c/Users/sgnka/AppData/Local/Obsidian/Obsidian.com"
VAULT="claude_vault"

# Single file
CONTENT=$(cat /path/to/file.md)
$OB create path="ProjectName/file.md" content="$CONTENT" vault=$VAULT overwrite

# Multiple files
for f in /path/to/files/*.md; do
    NAME=$(basename "$f")
    CONTENT=$(cat "$f")
    $OB create path="ProjectName/$NAME" content="$CONTENT" vault=$VAULT overwrite
done
```

## Workflow: Pull Notes to Local

```bash
$OB read file="My Note" vault=claude_vault > /tmp/my_note.md
$OB search query="dissertation" vault=Sync_vault format=json > /tmp/results.json
```

## Parameter Notes

- `file=<name>` resolves like wikilinks (by filename, no extension needed)
- `path=<path>` is exact from vault root (e.g., `folder/note.md`)
- Quote values with spaces: `name="My Note"`
- Use `\n` for newlines, `\t` for tabs in content values
- Most commands default to the active file when file/path is omitted

---

# Part 2: obsidian-headless (`ob` CLI)

Use when Obsidian app is not available (remote servers, HPC, CI/CD).

## Prerequisites

- `npm install -g obsidian-headless`
- Obsidian Sync subscription with a remote vault
- Node.js available

## Credentials

Stored in `~/.obsidian-sync-credentials` (chmod 600). **Never store in project directories or git.**

```bash
CRED_FILE="$HOME/.obsidian-sync-credentials"
if [ -f "$CRED_FILE" ]; then
    source "$CRED_FILE"
    # Contains: OB_EMAIL, OB_PASSWORD, OB_VAULT, OB_ENCRYPTION_PASSWORD
else
    echo "Create ~/.obsidian-sync-credentials with:"
    echo '  OB_EMAIL="your-email@example.com"'
    echo '  OB_PASSWORD="your-password"'
    echo '  OB_VAULT="vault-name"'
    echo '  OB_ENCRYPTION_PASSWORD="your-encryption-password"'
    echo "Then: chmod 600 ~/.obsidian-sync-credentials"
fi
```

### Login:
```bash
source "$HOME/.obsidian-sync-credentials"
ob login --email "$OB_EMAIL" --password "$OB_PASSWORD"
```

## Vault Structure Convention

```
VAULT_ROOT/
├── ProjectName/
│   ├── Main Index.md        ← index with [[wikilinks]] to sub-pages
│   └── subfolder/
│       ├── page-1.md
│       └── page-2.md
```

**Rules:**
1. One index page per project at project root with `[[wikilinks]]`
2. Detail pages in subfolders — keeps explorer clean
3. Use `[[subfolder/page-name]]` wikilinks from index
4. Add navigation breadcrumbs: `← [[prev]] | [[Main Index]] | [[next]] →`
5. Never dump files at vault root

## Sync Workflow

```bash
source "$HOME/.obsidian-sync-credentials"

# 1. List remote vaults
ob sync-list-remote

# 2. Prepare local structure
VAULT_DIR=/tmp/$(whoami)_obsidian
PROJECT="ProjectName"
mkdir -p "$VAULT_DIR/$PROJECT/subfolder"
cp index.md "$VAULT_DIR/$PROJECT/"
cp detail-pages/*.md "$VAULT_DIR/$PROJECT/subfolder/"

# 3. Setup and sync
ob sync-setup \
    --vault "$OB_VAULT" \
    --path "$VAULT_DIR" \
    --device-name my-device \
    --password "$OB_ENCRYPTION_PASSWORD"

ob sync --path "$VAULT_DIR"

# 4. Cleanup
rm -rf "$VAULT_DIR"
```

### HPC/NERSC Note

**SQLite WAL mode does not work on network filesystems (Lustre, GPFS).** SSH to a login node and use `/tmp`:

```bash
ssh -o BatchMode=yes login01 "
    export PATH=/global/homes/s/sgkayast/.conda/envs/pace_node/bin:\$PATH
    VAULT_DIR=/tmp/\$(whoami)_obsidian
    mkdir -p \"\$VAULT_DIR/ProjectName\"
    cp /path/to/files/*.md \"\$VAULT_DIR/ProjectName/\"
    ob sync-setup --vault '$OB_VAULT' --path \"\$VAULT_DIR\" --device-name nersc-login --password '$OB_ENCRYPTION_PASSWORD'
    ob sync --path \"\$VAULT_DIR\"
    rm -rf \"\$VAULT_DIR\"
"
```

## Error Handling

| Error | Cause | Fix |
|-------|-------|-----|
| `SQLITE_IOERR_SHMMAP` | Network filesystem | SSH to login node, use /tmp |
| `Failed to validate password` | Wrong encryption password | Check vault encryption password |
| `No vaults found` | No Sync subscription | Create vault in Obsidian app |
| `ob: command not found` | Not installed or not in PATH | `npm install -g obsidian-headless` |
| `CLI is not enabled` | Official CLI not turned on | Settings > General > Command line interface |

## Security Notes

- **Never** store credentials in project directories or git
- **Always** chmod 600 on credential files
- **Always** clean up /tmp vault copies after sync
