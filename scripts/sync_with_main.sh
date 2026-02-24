#!/usr/bin/env bash
set -euo pipefail

# Usage:
#   scripts/sync_with_main.sh [remote] [base-branch]
# Example:
#   scripts/sync_with_main.sh origin main

REMOTE="${1:-origin}"
BASE_BRANCH="${2:-main}"

if ! git rev-parse --is-inside-work-tree >/dev/null 2>&1; then
  echo "Not in a git repository" >&2
  exit 1
fi

if ! git remote get-url "$REMOTE" >/dev/null 2>&1; then
  echo "Remote '$REMOTE' not found. Add remote first." >&2
  exit 1
fi

echo "==> Fetching $REMOTE/$BASE_BRANCH"
git fetch "$REMOTE" "$BASE_BRANCH"

echo "==> Enabling rerere for repeated conflict auto-resolution"
git config rerere.enabled true
git config rerere.autoupdate true

echo "==> Rebasing current branch on $REMOTE/$BASE_BRANCH"
if git rebase "$REMOTE/$BASE_BRANCH"; then
  echo "Rebase completed without conflicts."
  exit 0
fi

echo "==> Conflict detected, applying deterministic auto-resolution rules"
while IFS= read -r file; do
  case "$file" in
    README.md|tests/*)
      git checkout --theirs -- "$file"
      ;;
    src/opentalons/*)
      git checkout --ours -- "$file"
      ;;
    *)
      # prefer ours by default for app-specific content
      git checkout --ours -- "$file"
      ;;
  esac
  git add "$file"
done < <(git diff --name-only --diff-filter=U)

if git rebase --continue; then
  echo "Rebase continued after auto-resolution."
else
  echo "Unable to auto-resolve all conflicts. Please run: git status" >&2
  exit 2
fi
