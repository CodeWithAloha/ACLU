#!/bin/bash
set -x # echo bash commands before execution, useful for debugging
set -e # stop bash execution on on first error

# Install dockers on every deploy...so that we can update it from code without having to re-provision
# Install and configure docker
DOCKER_COMPOSE_VERSION=1.15.0
# used convenience scripts since this is just test
# https://docs.docker.com/engine/installation/linux/docker-ce/debian/#install-using-the-convenience-script
sudo wget -qO- https://get.docker.com/ | sudo sh
# download docker-compose
# TODO - Add IF logic to check if docker is already installed
sudo wget -O /usr/local/bin/docker-compose https://github.com/docker/compose/releases/download/${DOCKER_COMPOSE_VERSION}/run.sh

# TODO - Remove this if unnecessary! Add r and x permissions to all users...
sudo chmod ugo+rx /usr/local/bin/docker-compose
