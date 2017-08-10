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
git clone https://github.com/codeforhawaii/aclu aclu
cd aclu
PATH=/usr/local/node/bin/:${PATH} yarn
