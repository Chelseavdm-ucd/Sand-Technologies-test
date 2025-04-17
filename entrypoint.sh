#!/bin/bash

REPO_URL=${REPO_URL:-https://github.com/YOUR-ORG/YOUR-REPO.git}
TARGET_DIR=/home/jovyan/work

echo "Cloning '$REPO_URL' into '$TARGET_DIR'..."

# If directory exists and is not a Git repo, remove it
if [ -d "$TARGET_DIR" ] && [ ! -d "$TARGET_DIR/.git" ]; then
    echo "Directory exists but is not a Git repo. Cleaning up..."
    rm -rf "$TARGET_DIR"
fi

# Clone the repo if it's not already there
if [ ! -d "$TARGET_DIR/.git" ]; then
    git clone $REPO_URL $TARGET_DIR
else
    echo "Repo already exists. Not touching branches."
fi

# Install requirements, if they're there
if [ -f "$TARGET_DIR/requirements.txt" ]; then
    echo "Installing Python dependencies..."
    pip install -r "$TARGET_DIR/requirements.txt"
fi

# launch JupyterLab
echo "Launching JupyterLab..."
exec start-notebook.sh
