#!/usr/bin/env bash

echo "===> Ensuring pipenv is installed"
pip3 install pipenv --upgrade
echo "===> Getting your environment set up"
pipenv install
echo "===> Moving Unit files as needed"

if [ ! -f /usr/lib/systemd/system/irflow-integrations-websvc.service ] ; then
    sudo cp irflow-integrations-websvc.service /usr/lib/systemd/system/
    sudo systemctl daemon-reload
fi

echo "===> Starting service"
./start_websvc.sh