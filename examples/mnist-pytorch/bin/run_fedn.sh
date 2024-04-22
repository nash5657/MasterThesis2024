#!/bin/bash

# Define the path to your Docker Compose YAML file
COMPOSE_FILE_PATH="/Users/nash/Project/fedn/fedn/docker-compose.yaml"

# Change to the directory where the Docker Compose file is located
cd $(dirname $COMPOSE_FILE_PATH)

# Run Docker Compose up
docker-compose -f $(basename $COMPOSE_FILE_PATH) up

# Alternatively, you can run Docker Compose without changing the directory:
# docker-compose -f $COMPOSE_FILE_PATH up
