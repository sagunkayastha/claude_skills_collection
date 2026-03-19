#!/usr/bin/env bash
# update_skills.sh
# Checks K-Dense-AI/claude-scientific-skills for new skills and downloads any we don't have.
# Skips skills from excluded categories (bioinformatics, cheminformatics, clinical, etc.)

set -euo pipefail

REPO="K-Dense-AI/claude-scientific-skills"
REMOTE_PATH="scientific-skills"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
EXCLUDED_CONF="$SCRIPT_DIR/excluded.conf"

# Load excluded skills from excluded.conf (ignore blank lines and comments)
mapfile -t EXCLUDED_SKILLS < <(grep -v '^\s*#' "$EXCLUDED_CONF" | grep -v '^\s*$')

is_excluded() {
  local skill="$1"
  for excluded in "${EXCLUDED_SKILLS[@]}"; do
    [[ "$excluded" == "$skill" ]] && return 0
  done
  return 1
}

# Get all skills currently installed (across all category subdirs)
get_installed_skills() {
  find "$SCRIPT_DIR" -mindepth 2 -maxdepth 2 -type d | xargs -I{} basename {}
}

echo "Fetching skill list from $REPO..."
remote_skills=$(gh api "repos/$REPO/contents/$REMOTE_PATH" --jq '.[].name')

installed_skills=$(get_installed_skills)

new_skills=()
skipped_excluded=()

while IFS= read -r skill; do
  if is_excluded "$skill"; then
    skipped_excluded+=("$skill")
    continue
  fi
  if echo "$installed_skills" | grep -qx "$skill"; then
    continue
  fi
  new_skills+=("$skill")
done <<< "$remote_skills"

echo ""
echo "Skipped (excluded categories): ${#skipped_excluded[@]}"
echo "Already installed: $(echo "$installed_skills" | wc -l | tr -d ' ')"
echo "New skills to download: ${#new_skills[@]}"

if [ ${#new_skills[@]} -eq 0 ]; then
  echo ""
  echo "Everything is up to date."
  exit 0
fi

echo ""
echo "New skills found:"
for skill in "${new_skills[@]}"; do
  echo "  - $skill"
done

echo ""
read -rp "Download all ${#new_skills[@]} new skill(s)? [y/N] " confirm
[[ "$confirm" =~ ^[Yy]$ ]] || { echo "Aborted."; exit 0; }

# Download to a temporary location, then move into the uncategorized folder
UNCATEGORIZED="$SCRIPT_DIR/uncategorized"
mkdir -p "$UNCATEGORIZED"

for skill in "${new_skills[@]}"; do
  echo "Downloading $skill..."
  tmp_dir=$(mktemp -d)
  gh api "repos/$REPO/contents/$REMOTE_PATH/$skill" --jq '.[].name' | while IFS= read -r filename; do
    content=$(gh api "repos/$REPO/contents/$REMOTE_PATH/$skill/$filename" --jq '.content' | base64 -d)
    echo "$content" > "$tmp_dir/$filename"
  done
  mv "$tmp_dir" "$UNCATEGORIZED/$skill"
  echo "  -> saved to uncategorized/$skill"
done

echo ""
echo "Done! ${#new_skills[@]} new skill(s) downloaded to: $UNCATEGORIZED"
echo "Move them into the appropriate category folder when ready."
