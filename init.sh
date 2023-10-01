#!/bin/bash

IMAGE_NAME="optimalknight/gitasage"
TAG="latest"

HOST_PORT=8501
CONTAINER_PORT=8501

docker run -d -p $HOST_PORT:$CONTAINER_PORT $IMAGE_NAME:$TAG

sleep 3

open http://localhost:$HOST_PORT 2>/dev/null

