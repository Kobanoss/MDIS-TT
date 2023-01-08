#!/bin/sh

cd server

docker-compose down --volumes --rmi all

echo "\033[92m"">> Server deleting script completed!"
