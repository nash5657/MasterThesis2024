#!/bin/bash

# Kill and remove all containers with names starting with "client"
docker kill $(docker ps -aq --filter "name=client")
docker rm $(docker ps -aq --filter "name=client")

# Kill and remove all containers with names starting with "fedn"
docker kill $(docker ps -aq --filter "name=fedn")
docker rm $(docker ps -aq --filter "name=fedn")
