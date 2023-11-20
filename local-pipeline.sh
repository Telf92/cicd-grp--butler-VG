#! /bin/bash


echo "=============
  Create and activate Venv  
=============" 

python3 -m venv backend/venv
source backend/venv/bin/activate
pip install -r backend/requirements.txt

echo "=============
  Run Black  
=============" 

black backend/

echo "=============
  Run PyLint  
============="

python3 -m pylint --fail-under=7 --recursive true --ignore=venv backend

echo "=============
  Build Docker Image  
============="

docker build -t ping-url .

echo "=============
  Run Docker Image  
============="

CONTAINER_ID=$(docker run --network=host -d ping-url)
sleep 3

echo "=============
  Run Tests  
============="

pytest backend/tests/test_api_request.py
pytest backend/pingurl/test_*

echo "=============
  Stop and Remove Containers  
============="

docker stop $CONTAINER_ID
docker rm $CONTAINER_ID