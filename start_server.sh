#!/bin/sh

cd server

docker-compose build --no-cache

docker-compose up -d
sleep 3.5

echo "\033[92m"">> Server started succesfully!"