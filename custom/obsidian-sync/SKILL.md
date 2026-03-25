---
name: obsidian-sync
description: Sync files to Obsidian vault via obsidian-headless (ob CLI). Use when the user says "sync to obsidian", "push to obsidian", "upload to vault", or wants to share markdown/notes with their Obsidian vault. Handles login, vault setup, and file syncing automatically.
license: MIT
metadata:
  skill-author: sagunkayastha
  version: 1.0.0
  tags: [obsidian, sync, notes, vault]
  dependencies: [obsidian-headless]
---

# Obsidian Sync Skill

Sync local files to a remote Obsidian vault using the `ob` CLI (obsidian-headless).

## When to Use

- User says "sync to obsidian", "push to obsidian", "upload to vault"
- User wants markdown files available in their Obsidian vault
- User wants to share diagrams, notes, or docs via Obsidian

## Prerequisites

- `obsidian-headless` npm package installed globally
- Obsidian Sync subscription with a remote vault
- Node.js available

## Setup Check

**Always run this check first before any sync operation:**

```bash
# 1. Verify ob CLI is available
OB_PATH=$(which ob 2>/dev/null)
if [ -z "$OB_PATH" ]; then
    # Try known Node.js paths
    export PATH="/global/homes/s/sgkayast/.conda/envs/pace_node/bin:$PATH"
    OB_PATH=$(which ob 2>/dev/null)
fi

if [ -z "$OB_PATH" ]; then
    echo "ob CLI not found. Install with: npm install -g obsidian-headless"
    exit 1
fi

# 2. Check login status
ob login 2>&1
```

If not logged in, the credentials file is needed (see Credentials section below).

## Credentials

Credentials are stored in `~/.obsidian-sync-credentials` (chmod 600). **Never store credentials in project directories or git repos.**

### Check for existing credentials:
```bash
CRED_FILE="$HOME/.obsidian-sync-credentials"
if [ -f "$CRED_FILE" ]; then
    source "$CRED_FILE"
    # File contains: OB_EMAIL="..." and OB_PASSWORD="..."
else
    echo "No credentials found."
    echo "Please create ~/.obsidian-sync-credentials with:"
    echo '  OB_EMAIL="your-email@example.com"'
    echo '  OB_PASSWORD="your-password"'
    echo "Then run: chmod 600 ~/.obsidian-sync-credentials"
    # ASK the user to provide email and password
    # Write the file for them, then chmod 600
fi
```

### Login with credentials:
```bash
source "$HOME/.obsidian-sync-credentials"
ob login --email "$OB_EMAIL" --password "$OB_PASSWORD"
```

## Sync Workflow

### Step 1: Determine what to sync
Ask the user what files/folders to sync and where in the vault they should go (subfolder name).

### Step 2: List remote vaults
```bash
ob sync-list-remote
```
If multiple vaults exist, ask the user which one. If only one, use it.

### Step 3: Sync files

**IMPORTANT: SQLite WAL mode does not work on network/parallel filesystems (Lustre, GPFS, CFS). On NERSC or similar HPC systems, you MUST SSH to a login node and use /tmp for the local vault path.**

```bash
# On NERSC: must SSH to login node for SQLite compatibility
ssh -o BatchMode=yes login01 "
    export PATH=/global/homes/s/sgkayast/.conda/envs/pace_node/bin:\$PATH

    # Create temp vault dir with target subfolder
    VAULT_DIR=/tmp/\$(whoami)_obsidian
    SUBFOLDER=\"\${VAULT_DIR}/TARGET_SUBFOLDER\"
    mkdir -p \"\$SUBFOLDER\"

    # Copy files to sync
    cp /path/to/files/*.md \"\$SUBFOLDER/\"

    # Setup and sync
    ob sync-setup \\
        --vault VAULT_NAME \\
        --path \"\$VAULT_DIR\" \\
        --device-name nersc-login \\
        --password 'ENCRYPTION_PASSWORD' 2>&1

    ob sync --path \"\$VAULT_DIR\" 2>&1

    # Cleanup temp dir
    rm -rf \"\$VAULT_DIR\"
"
```

### Step 4: Verify
Check output for `Fully synced` and `Upload complete` messages for each file.

## Common Operations

### Push files to a subfolder
```bash
# Files go to PACE_Pipeline/ in the vault
SUBFOLDER="PACE_Pipeline"
```

### Push a single file
```bash
cp /path/to/file.md "$VAULT_DIR/$SUBFOLDER/"
ob sync --path "$VAULT_DIR"
```

### Delete files from vault
```bash
# Sync first to pull current state, delete locally, re-sync
ob sync --path "$VAULT_DIR"
rm "$VAULT_DIR/target_file.md"
ob sync --path "$VAULT_DIR"
```

### List what's in the vault
```bash
ob sync --path "$VAULT_DIR"  # pulls everything
ls -R "$VAULT_DIR"
```

## Error Handling

| Error | Cause | Fix |
|-------|-------|-----|
| `SQLITE_IOERR_SHMMAP` | Network filesystem (Lustre/GPFS) | SSH to login node, use /tmp |
| `Failed to validate password` | Wrong encryption password | Ask user for vault encryption password |
| `No vaults found` | No Sync subscription or no remote vaults | User needs to create vault in Obsidian app |
| `ob: command not found` | Not installed or not in PATH | `npm install -g obsidian-headless` |

## Security Notes

- **Never** store credentials in project directories
- **Never** commit credentials to git
- **Always** use chmod 600 on credential files
- **Always** clean up /tmp vault copies after sync
- If user puts credentials in a project file, **delete it immediately** and create the proper credential file instead
