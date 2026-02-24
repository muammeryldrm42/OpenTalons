#!/usr/bin/env bash
set -euo pipefail

# Resolve currently-open git conflicts in merge/rebase/cherry-pick state.
# Useful when GitHub shows: "This branch has conflicts that must be resolved".
#
# Usage:
#   scripts/resolve_conflicts_now.sh
#   scripts/resolve_conflicts_now.sh --dry-run

DRY_RUN=false
if [[ "${1:-}" == "--dry-run" ]]; then
  DRY_RUN=true
fi

if ! git rev-parse --is-inside-work-tree >/dev/null 2>&1; then
  echo "Not in a git repository" >&2
  exit 1
fi

unresolved="$(git diff --name-only --diff-filter=U)"
if [[ -z "$unresolved" ]]; then
  echo "No unresolved conflict files found."
  exit 0
fi

choose_side() {
  local file="$1"
  case "$file" in
    README.md|tests/*)
      echo "theirs"
      ;;
    src/opentalons/*)
      echo "ours"
      ;;
    *)
      echo "ours"
      ;;
  esac
}

echo "Resolving unresolved files with deterministic rules:"
while IFS= read -r file; do
  [[ -z "$file" ]] && continue
  side="$(choose_side "$file")"
  echo "  - $file => $side"

  if [[ "$DRY_RUN" == true ]]; then
    continue
  fi

  if [[ "$side" == "theirs" ]]; then
    git checkout --theirs -- "$file"
  else
    git checkout --ours -- "$file"
  fi
  git add "$file"
done <<< "$unresolved"

if [[ "$DRY_RUN" == true ]]; then
  echo "Dry run only. No files changed."
  exit 0
fi

# Continue the active git operation if any.
if [[ -d .git/rebase-merge || -d .git/rebase-apply ]]; then
  echo "Detected rebase state. Running: git rebase --continue"
  git rebase --continue || true
elif [[ -f .git/MERGE_HEAD ]]; then
  echo "Detected merge state. Create merge commit with:"
  echo "  git commit -m \"Resolve conflicts\""
elif [[ -f .git/CHERRY_PICK_HEAD ]]; then
  echo "Detected cherry-pick state. Running: git cherry-pick --continue"
  git cherry-pick --continue || true
else
  echo "Conflicts staged. Finish with your preferred git command."
fi
