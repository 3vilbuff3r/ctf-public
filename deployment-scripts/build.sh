#!/bin/bash

# Expects a "dev" directory in the current directory. Which has the git repo.

# Print commands, exit on error.
set -x
set -e

cd dev

pushd use-the-source
docker build . -t source:dv1
popd

pushd mr-robot
docker build . -t robot:dv1
popd

pushd oom-nom
docker build . -t oomnom:dv1
popd

pushd binging
docker build . -t binging:dv1
popd

pushd path-to-heaven
docker build . -t heaven:dv1
popd

pushd ping-pong
docker build . -t ping:dv1
popd

pushd ouch
docker build . -t sqli:dv1
popd

pushd flags-sale
docker build . -t sale:dv1
popd

pushd netcat
docker build . -t netcat:dv1
popd

pushd matrix
docker build . -t matrix:dv1
popd

echo "Build finished."