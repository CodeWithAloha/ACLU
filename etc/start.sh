#!/bin/bash

sudo sg vagrant <<\DEVOPS_BLOCK
    cd /var/project-aclu/backend
    docker-compose up -d
DEVOPS_BLOCK

cd /var/project-aclu/frontend
PATH=/usr/local/node/bin/:${PATH} yarn run dev&
