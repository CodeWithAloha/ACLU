#!/bin/bash
set -ex

sudo apt-get update
sudo apt-get install -y git

# Donwnload and unpack node into /usr/local
cd /usr/local
sudo rm -rf /usr/local/node-v8.3.0-linux-x64 /usr/local/node
wget -qO- https://nodejs.org/dist/v8.3.0/node-v8.3.0-linux-x64.tar.xz | sudo tar xvJ
sudo ln -s /usr/local/node-v8.3.0-linux-x64 /usr/local/node

# install yarn
sudo env "PATH=/usr/local/node/bin/:${PATH}" npm install -g yarn

# add /usr/local/node to user vagrant's path
cd ${HOME}
echo HOME=${HOME}
echo "export PATH=/usr/local/node/bin/:${PATH}" >> .profile
cd /var/project-aclu/frontend
PATH=/usr/local/node/bin/:${PATH} yarn

# install the dockers
sudo apt-get remove docker docker.io 2>/dev/null

## used convenience scripts since this is just test -> https://docs.docker.com/engine/installation/linux/docker-ce/debian/#install-using-the-convenience-script
wget -qO- https://get.docker.com/ | sudo sh

sudo usermod -aG docker vagrant

sudo wget -O /usr/local/bin/docker-compose https://github.com/docker/compose/releases/download/1.15.0/run.sh && sudo chmod +x /usr/local/bin/docker-compose

sudo sg vagrant <<\DEVOPS_BLOCK
    cd /var/project-aclu/backend/docker
    # docker-compose build
    # docker-compose up -d

    # PROFIT
    # curl localhost:5000/aloha
DEVOPS_BLOCK
