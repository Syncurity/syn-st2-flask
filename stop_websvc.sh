#!/usr/bin/env bash

systemctl is-active --quiet irflow-integrations-websvc
retVal=$?
if [[ ${retVal} -ne 0 ]]; then
    echo "===> Service already stopped!"
else
    echo "===> Stopping Integrations Webservice"
    sudo systemctl stop irflow-integrations-websvc
fi

exit ${retVal}
