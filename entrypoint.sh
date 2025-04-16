#!/bin/bash

# Set repo details via env vars or use defaults
REPO_URL=${REPO_URL:-https://github.com/YOUR-ORG/YOUR-REPO.git}
BRANCH=${GIT_BRANCH:-main}
TARGET_DIR=/home/jovyan/work

echo "Pulling branch '$BRANCH' from '$REPO_URL'..."

# If directory exists and isn't a git repo, remove it
if [ -d "$TARGET_DIR" ] && [ ! -d "$TARGET_DIR/.git" ]; then
    echo "existing folder at $TARGET_DIR is not a Git repo. Removing it..."
    rm -rf "$TARGET_DIR"
fi

# If not already cloned, clone it
if [ ! -d "$TARGET_DIR/.git" ]; then
    git clone --branch $BRANCH $REPO_URL $TARGET_DIR
else
    echo "Repo already present. Pulling latest changes..."
    cd $TARGET_DIR
    git fetch origin $BRANCH
    git checkout $BRANCH
    git pull
fi

# If requirements.txt exists, install them
if [ -f "$TARGET_DIR/requirements.txt" ]; then
    echo "Installing Python dependencies..."
    pip install -r "$TARGET_DIR/requirements.txt"
fi

# Start Jupyter
echo "launching Jupyter..."
exec start-notebook.sh
