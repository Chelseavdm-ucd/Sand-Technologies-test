FROM jupyter/base-notebook:latest

# Switch to root to install system packages and handle file permissions
USER root

# Install git
RUN apt-get update && apt-get install -y git && rm -rf /var/lib/apt/lists/*

# Copy entrypoint script and make it executable
COPY entrypoint.sh /usr/local/bin/entrypoint.sh
RUN chmod +x /usr/local/bin/entrypoint.sh

# Switch back to jovyan user for the rest of the operations
USER $NB_UID

# Add and install Python dependencies during build
COPY requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt

WORKDIR /home/jovyan

ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]
