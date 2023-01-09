#!/bin/sh

cd server

docker-compose down --volumes --rmi all

echo -e "\033[92m>> Server REMOVE script completed!$(tput sgr 0)"
