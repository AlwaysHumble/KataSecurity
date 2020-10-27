#!/bin/bash
CONTAINER_NAME=$1
TEST_CASE=$2
DOCKER_PATH="/usr/bin"
PATH="/home/karan/KataSecurity/test_cases"
cd $DOCKER_PATH
./docker create --name $CONTAINER_NAME -it ubuntu
echo "$CONTAINER_NAME created"
./docker start $CONTAINER_NAME
./docker cp $PATH/$TEST_CASE $CONTAINER_NAME:/$TEST_CASE
echo "$CONTAINER_NAME copied"