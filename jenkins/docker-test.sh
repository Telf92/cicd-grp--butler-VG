#! /bin/bash

CONTAINER=$(docker run -dp 5000:5000 ping)
sleep 3

# Python script
pytest

docker kill $CONTAINER
docker rm $CONTAINER