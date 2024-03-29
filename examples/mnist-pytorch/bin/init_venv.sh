#!/bin/bash
set -e

# Init venv
python -m venv .mnist-pytorch

# Pip deps
.mnist-pytorch/bin/pip install --upgrade pip
.mnist-pytorch/bin/pip install -e /Users/nash/Project/fedn/fedn/fedn 
.mnist-pytorch/bin/pip install -r requirements.txt
