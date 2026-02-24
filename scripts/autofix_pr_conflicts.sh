#!/usr/bin/env bash
set -euo pipefail

# Auto-merge base branch into current branch and resolve conflicts deterministically.
# Intended for CI usage (e.g. GitHub Actions) or local execution.
#
# Usage:
#   scripts/autofix_pr_conflicts.sh <base-branch>
# Example:
#   scripts/autofix_pr_conflicts.sh main

BASE_BRANCH="${1:-main}"

if ! git rev-parse --is-inside-work-tree >/dev/null 2>&1; then
  echo "Not in a git repository" >&2
  exit 1
fi

# Ensure base branch ref exists locally.
git fetch origin "$BASE_BRANCH":"refs/remotes/origin/$BASE_BRANCH"

# Attempt merge. If no conflict, merge commit is created (or already up to date).
if git merge --no-edit "origin/$BASE_BRANCH"; then
  echo "Merge completed without conflicts."
  exit 0
fi

unresolved="$(git diff --name-only --diff-filter=U)"
if [[ -z "$unresolved" ]]; then
  echo "Merge failed but no unresolved files were found." >&2
  exit 2
fi

echo "Applying deterministic conflict rules..."
while IFS= read -r file; do
  [[ -z "$file" ]] && continue
  case "$file" in
    README.md|tests/*)
      git checkout --theirs -- "$file"
      ;;
    src/opentalons/*)
      git checkout --ours -- "$file"
      ;;
    *)
      git checkout --ours -- "$file"
      ;;
  esac
  git add "$file"
done <<< "$unresolved"

git commit -m "Auto-resolve PR conflicts against $BASE_BRANCH"
echo "Conflicts resolved and merge commit created."
