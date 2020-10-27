#!/bin/bash
CONTAINER_NAME=$1
TEST_CASE=$2
DOCKER_PATH="/usr/bin"
cd $DOCKER_PATH
PATH="/home/karan/KataSecurity/test_cases"
./docker exec -it $CONTAINER_NAME ls
