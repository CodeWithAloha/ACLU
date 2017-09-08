#!/bin/bash
set -x # echo bash commands before execution, useful for debugging
set -e # stop bash execution on on first error

NODE_VERSION=8.1.4 # latest Node version as of 15-Aug-2017
JQ_VERSION=1.5 # latest jq version as of 15-Aug-2015
DOCKER_COMPOSE_VERSION=1.15.0

sudo apt-get update
sudo apt-get install -y \
     python-pip \
     git \
     httpie \
     gdal-bin


# install ./jq (https://stedolan.github.io/jq/)
sudo wget -O /usr/local/bin/jq https://github.com/stedolan/jq/releases/download/jq-${JQ_VERSION}/jq-linux64
sudo chmod a+x /usr/local/bin/jq

# nuke any previous versions of node in /usr/local/node
sudo rm -rf /usr/local/node-*-linux-x64 /usr/local/node

# donwnload and unpack node into /usr/local
cd /usr/local
wget -qO- https://nodejs.org/dist/v${NODE_VERSION}/node-v${NODE_VERSION}-linux-x64.tar.xz | sudo tar xvJ
sudo ln -s /usr/local/node-v${NODE_VERSION}-linux-x64 /usr/local/node

# install yarn
sudo env "PATH=/usr/local/node/bin/:${PATH}" npm install -g yarn@">=1.0.0"

# add /usr/local/node to user vagrant's path
echo "export PATH=/usr/local/node/bin/:${PATH}" >> ${HOME}/.profile

# Install the node_packages using yarn (not npm)
cd /var/project-aclu/frontend
PATH=/usr/local/node/bin/:${PATH} yarn

# install the dockers
sudo apt-get remove docker docker.io 2>/dev/null

# used convenience scripts since this is just test
# https://docs.docker.com/engine/installation/linux/docker-ce/debian/#install-using-the-convenience-script
wget -qO- https://get.docker.com/ | sudo sh

# add user vagrant to the docker group to allow vagrant to run docker commands
sudo usermod -aG docker vagrant

# download docker-compose
sudo wget -O /usr/local/bin/docker-compose https://github.com/docker/compose/releases/download/${DOCKER_COMPOSE_VERSION}/run.sh
sudo chmod +x /usr/local/bin/docker-compose

# docker in vm, disabled for now
sudo sg vagrant <<\DEVOPS_BLOCK
    cd /var/project-aclu/backend
    docker-compose build
DEVOPS_BLOCK
