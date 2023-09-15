FROM python:3.11-slim-bookworm
LABEL author="manwe"
LABEL description="An example Dockerfile"

ENV NAME="Manwe"
ARG DOCKER_USER=default_user

RUN apt update && \
    # cd /app/ && \
    apt install sudo && \
    sudo adduser --system --group $DOCKER_USER
USER $DOCKER_USER

COPY hello-world.py /app/
CMD bash