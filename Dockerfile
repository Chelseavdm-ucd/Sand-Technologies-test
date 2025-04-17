FROM jupyter/base-notebook:latest

# Install system packages
RUN apt-get update && apt-get install -y git

# Copy entrypoint script
COPY entrypoint.sh /usr/local/bin/entrypoint.sh
RUN chmod +x /usr/local/bin/entrypoint.sh

# Add and install Python dependencies during build
COPY requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt

# Set workdir
WORKDIR /home/jovyan

# Entrypoint
ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]
