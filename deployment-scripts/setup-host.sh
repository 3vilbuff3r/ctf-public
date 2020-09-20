#!/bin/bash

# Script assumes a ubuntu server defualt azure installation and creates a kubernetes host.
# Assumes sudo access if without password.

sudo apt-get install docker.io net-tools wget curl 
sudo usermod -G docker $USER
