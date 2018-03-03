#!/bin/bash
set -x # echo bash commands before execution, useful for debugging
set -e # stop bash execution on on first error

# Upgrade aws cli to support --no-include-email for docker login (email was deprecated from docker)
pip install --upgrade awscli
#$(aws ecr get-login --region $ECR_REGION --no-include-email)
$(aws ecr get-login --region us-west-2 --no-include-email) # Ended up harcoding REGION here...if it ever changes we need to update the script

# Get latest version of image
cd /var/project-aclu/
docker image rmi "705750910119.dkr.ecr.us-west-2.amazonaws.com/aclu:latest"
docker pull "705750910119.dkr.ecr.us-west-2.amazonaws.com/aclu:latest"