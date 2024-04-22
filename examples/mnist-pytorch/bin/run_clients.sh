#!/bin/bash

# Check for at least one argument
if [ "$#" -lt 1 ]; then
    echo "Usage: $0 <number_of_clients>"
    exit 1
fi

NUM_CLIENTS=$1

# Define the directory where your files are located
DIR="/Users/nash/Project/fedn/fedn/examples/mnist-pytorch"

# Ensure Docker network exists
if ! docker network ls | grep -q fedn_default; then
  docker network create fedn_default
fi

# Change to the directory
cd $DIR

# Start multiple clients in the background
for (( i=1; i<=NUM_CLIENTS; i++ ))
do
    docker run -d \
    -v $PWD/client.yaml:/app/client.yaml \
    -v $PWD/data/clients/$i:/var/data \
    -v $PWD/rouge_dataset.csv:/app/data/rouge_dataset.csv \
    -e ENTRYPOINT_OPTS=--data_path=/var/data/dataset.pt \
    --network=fedn_default \
    llm:latest run client -in client.yaml --name client$i &
done
