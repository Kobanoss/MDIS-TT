#!/bin/sh

cd server

docker-compose build --no-cache

echo "\033[92m"">> Server start script completed!"
