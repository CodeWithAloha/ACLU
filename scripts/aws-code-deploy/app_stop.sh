#!/bin/bash
# Stop running docker
cd /var/project-aclu/
# Stop the running "aclu-api" container if there is one
CONTAINER_NAME="aclu-api"
CONTAINER_ID="$(docker ps --all --quiet --filter=name="$CONTAINER_NAME")"
if [ -n "$CONTAINER_ID" ]; then
  docker stop $CONTAINER_ID && docker rm $CONTAINER_ID || true
fi