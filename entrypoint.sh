#!/bin/bash
set -e

REPO_URL="https://github.com/Chelseavdm-ucd/Sand-Technologies-test"
TARGET_DIR="/home/jovyan/work"

if [ ! -d "$TARGET_DIR/.git" ]; then
    git clone "$REPO_URL" "$TARGET_DIR"
else
    echo "Repo already exists."
fi

exec "$@"
