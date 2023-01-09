#!/bin/sh

cd server

docker-compose stop

echo -e "\033[92m>> Server STOP script completed!$(tput sgr 0)"
