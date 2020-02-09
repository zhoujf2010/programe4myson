#!/bin/bash

TOOLS_PATH="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

cd $TOOLS_PATH/..

echo "Building docker image"

docker build -t edublocks .
