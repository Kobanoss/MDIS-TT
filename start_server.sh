#!/bin/sh

cd server

docker-compose up -d
sleep 3.5

echo -e "\033[92m>> Server START script completed!$(tput sgr 0)"
