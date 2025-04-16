#!/bin/bash

REQ_FILE="/home/jovyan/work/requirements.txt"

echo "Checking for updated branch specific requirements.txt..."

if [ -f "$REQ_FILE" ]; then
  echo "Installing updated branch specific dependencies..."
  pip install --no-cache-dir -r "$REQ_FILE" || echo "Warning,  some packages failed to install."
else
  echo  " No extra requirements.txt found ...continuing with base environment."
fi

echo " Starting JupyterLab..."
exec "$@"
