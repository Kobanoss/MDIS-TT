#!/bin/sh

APP_FOLDER="MDIS-client"

cd "/usr/bin/$APP_FOLDER"
source "./venv/bin/activate"
echo -e "\033[92m>> Starting application...$(tput sgr 0)"
python "app.py"
deactivate

echo -e "\033[92m>> Application closed.$(tput sgr 0)"
