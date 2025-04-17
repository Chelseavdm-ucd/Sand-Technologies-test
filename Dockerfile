FROM jupyter/base-notebook:latest

# Switch to root to install system packages
USER root

RUN apt-get update && apt-get install -y git && rm -rf /var/lib/apt/lists/*

# Switch back to jovyan 
USER $NB_UID

# Copy entrypoint script
COPY entrypoint.sh /usr/local/bin/entrypoint.sh
RUN chmod +x /usr/local/bin/entrypoint.sh

# install Python dependencies during build
COPY requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt

# set directory
WORKDIR /home/jovyan

ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]
