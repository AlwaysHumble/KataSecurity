#!/bin/bash
CONTAINER_NAME=$1
DOCKER_PATH="/usr/bin"
cd $DOCKER_PATH
./docker rm $(docker stop $(docker ps -a -q --filter="name=$CONTAINER_NAME"))
echo "$CONTAINER_NAME removed"
