#!/usr/bin/env bash

systemctl is-active --quiet irflow-integrations-websvc
retVal=$?
if [[ ${retVal} -ne 0 ]]; then
    echo "===> Starting Integrations Webservice"
    sudo systemctl enable irflow-integrations-websvc
    sudo systemctl start irflow-integrations-websvc
else
    echo "===> Service already running!"
fi

exit ${retVal}
