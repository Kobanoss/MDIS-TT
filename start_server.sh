#!/bin/sh

cd server

docker-compose up -d
sleep 3.5

echo "\033[92m"">> Server start script completed!"
