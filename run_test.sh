#!/bin/sh

#CURRENT_DIR="$(dirname "$(readlink -f $0)")"

#cd "$CURRENT_DIR"
ls
docker-compose build

docker-compose up