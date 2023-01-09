#!/bin/sh

APP_FOLDER="MDIS-client"

version=$(python -V 2>&1 | grep -Po '(?<=Python )(.+)')
parsedVersion=$(echo "${version//./}")

if [[ $parsedVersion -lt "3100" ]]
then
	echo -e "\032[92m>> Required Python 3.10+ to build the application$(tput sgr 0)"
    exit 1
fi

echo "Creating directory..."
mkdir "/usr/bin/$APP_FOLDER/"

echo "Copy files from source to /usr/bin/$APP_FOLDER..."
cp -R './gui-client/source/'* "/usr/bin/$APP_FOLDER/"

echo "Creating && activating virtualenv..."
python -m venv "/usr/bin/$APP_FOLDER/venv"
source "/usr/bin/$APP_FOLDER/venv/bin/activate"

echo "Loading modules..."
pip install -r /usr/bin/$APP_FOLDER/requirements.txt
deactivate

echo -e "\033[92m>> Build script completed!$(tput sgr 0)"
