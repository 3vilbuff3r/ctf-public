#!/bin/bash

# Print commands, exit on error.
set -x
set -e
# Get the minikube dev env.

# Source
docker run -p 8000:80 source:dv1 &> /tmp/docker.log &

# Robots.
docker run -p 8001:80 robot:dv1 &> /tmp/docker.log &

# Oom Nom Nom chall.
docker run -p 8002:80 oomnom:dv1 &> /tmp/docker.log & 

# Binging.
docker run -p 8003:80 binging:dv1 &> /tmp/docker.log &

# Heaven.
docker run -p 8004:80 heaven:dv1 &> /tmp/docker.log &

# ping.
docker run -p 8005:80 ping:dv1 &> /tmp/docker.log &

# sqli
docker run -p 8006:80 sqli:dv1 &> /tmp/docker.log &

# # Ouch3.
# kubectl run heaven --image=heaven:dv1 &> /tmp/docker.log &

# Flags Sale.
docker run -p 12000:20000 sale:dv1 &> /tmp/docker.log &

# NetCat.
docker run -p 12001:20000 netcat:dv1 &> /tmp/docker.log &

# Matrix.
docker run -p 12002:20000 matrix:dv1 &> /tmp/docker.log & 

# Setup port forward

