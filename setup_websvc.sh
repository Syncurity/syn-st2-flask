#!/usr/bin/env bash

echo "===> Ensuring pipenv is installed"
pip3 install -q --user pipenv --upgrade
echo "===> Getting your environment set up"
pipenv install > /dev/null
echo "===> Moving Unit files as needed"

if [ ! -f /usr/lib/systemd/system/irflow-integrations-websvc.service ] ; then
    sudo cp irflow-integrations-websvc.service /usr/lib/systemd/system/
    sudo systemctl daemon-reload
    echo "===> Starting service"
    ./start_websvc.sh
else
    echo "===> Service already set up, nothing to do!"
    exit 1
fi
