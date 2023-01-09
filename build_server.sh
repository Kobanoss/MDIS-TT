#!/bin/sh

cd server

docker-compose build --no-cache

echo -e "\033[92m>> Server BUILD script completed!$(tput sgr 0)"
