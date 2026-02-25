#!/usr/bin/env bash
set -euo pipefail

REPO_URL="https://github.com/openclaw/openclaw"
ARCHIVE_URL="https://codeload.github.com/openclaw/openclaw/tar.gz/refs/heads/main"
WORKDIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
TMP_DIR="$(mktemp -d)"

cleanup() {
  rm -rf "$TMP_DIR"
}
trap cleanup EXIT

echo "[info] Downloading upstream archive: $ARCHIVE_URL"
if ! curl -fsSL "$ARCHIVE_URL" -o "$TMP_DIR/openclaw.tar.gz"; then
  echo "[error] Unable to download OpenClaw archive. Check network/proxy access to GitHub." >&2
  exit 1
fi

tar -xzf "$TMP_DIR/openclaw.tar.gz" -C "$TMP_DIR"
SRC_DIR="$(find "$TMP_DIR" -maxdepth 1 -type d -name 'openclaw-*' | head -n 1)"

if [[ -z "${SRC_DIR:-}" ]]; then
  echo "[error] Downloaded archive did not contain expected openclaw directory." >&2
  exit 1
fi

cd "$WORKDIR"

echo "[info] Removing current tracked files (excluding .git)"
find . -mindepth 1 -maxdepth 1 \
  ! -name .git \
  ! -name .gitignore \
  -exec rm -rf {} +

echo "[info] Copying OpenClaw files into repository"
cp -a "$SRC_DIR"/. .

echo "[ok] Repository has been mirrored from $REPO_URL"
