#!/usr/bin/env python3
""" WSGI for the IR-Flow Integrations Webservice

Example::

    `$ ./wsgi.py`


"""
from integrations_websvc import app

if __name__ == '__main__':
    app.run(host=app.config['IP'], port=app.config['PORT'])

application = app
