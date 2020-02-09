#!/bin/bash

TOOLS_PATH="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

cd $TOOLS_PATH/..

echo "Running docker image"

docker run -it --rm -v $PWD:/var/edublocks -p 8081:8081 --name edublocks edublocks
