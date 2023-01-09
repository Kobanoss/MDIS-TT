# Execute to make all shell-scripts executable:
    sudo chmod +x xscripts.sh && ./xscripts.sh

# Server-part

## To run dockerized version of server, execute:
    ./build_server.sh && ./start_server.sh

#### To build dockerized version of server, execute:
    ./build_server.sh

#### To start dockerized version of server, execute:
    ./start_server.sh
    
#### To stop dockerized version of server, execute:
    ./stop_server.sh

#### To remove dockerized version of server, execute:
    ./kill_server.sh


# GUI-part

##  To run application, execute:
    sudo ./build_desktop_app.sh && ./start_desktop_app

#### To build application, execute:
    sudo ./build_desktop_app.sh

#### To start application, execute:
    ./start_desktop_app.sh

#### To remove application, execute:
    sudo ./remove_desktop_app.sh
    
# Configuration files:
`For GUI-client before build`   
    ./gui-client/source/config/app.json

`For GUI-client after build`    
    /usr/bin/MDIS-client/config/app.json
    
`For NGINX`                     
    ./server/services/nginx/nginx.conf

`For API`                       
    ./server/services/env/api.env
    
`For Postgres database`         
    ./server/services/env/postgres.env

`For Cloudbeaver`               
    ./server/services/env/dbeaver.env

`For Websocket`                 
    ./server/services/env/websocket.env

`For Web Application`           
    ./server/services/env/application.env
    
`Docker-compose`                
    ./server/docker-compose.yaml
