FROM ubuntu:22.04

ENV TZ="America/New_York"

ARG DEBIAN_FRONTEND=noninteractive

RUN apt update && apt upgrade -y && apt install software-properties-common -y
RUN add-apt-repository ppa:deadsnakes/ppa
RUN apt install python3.11 python3-pip -y
RUN python3 -m pip install --upgrade pip
RUN pip install pipenv

RUN apt update && apt upgrade -y
RUN apt install curl zip wget -y

# Installing the CLI (not the daemon) in order to enable the Prefect worker running on local dev machines to start workflow task containers.
ENV DOCKER_CLI_PACKAGE=docker-ce-cli_26.1.4-1~ubuntu.22.04~jammy_amd64
RUN curl -O https://download.docker.com/linux/ubuntu/dists/jammy/pool/stable/amd64/$DOCKER_CLI_PACKAGE.deb
RUN dpkg -i $DOCKER_CLI_PACKAGE.deb

WORKDIR /app

COPY libs/print_version.pex /app/
RUN PEX_TOOLS=1 python3 /app/print_version.pex venv --compile /app
