FROM jupyter/base-notebook

USER root
RUN apt-get update && apt-get install -y git
USER jovyan

COPY entrypoint.sh /usr/local/bin/entrypoint.sh
RUN chmod +x /usr/local/bin/entrypoint.sh

# Optional default workdir
WORKDIR /home/jovyan

# Use the custom entrypoint
ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]
