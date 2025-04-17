FROM jupyter/base-notebook

USER root
RUN apt-get update && apt-get install -y git

COPY entrypoint.sh /usr/local/bin/entrypoint.sh
RUN chmod +x /usr/local/bin/entrypoint.sh


WORKDIR /home/jovyan

USER jovyan

#custom entrypoint
ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]
