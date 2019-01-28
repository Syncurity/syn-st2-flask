Integrations Webservice
=======================

This repo contains the source for the Integrations Framework Webservice that presently provides support for integrations
that rely on a remote static file for dynamically ingesting threat information.

Installing the webservice
-------------------------

Make sure you have Pipenv_ installed, and clone this repository at the same level as your irflow-integrations repository.

.. code-block:: shell

    .
    └── Syncurity
        ├── irflow-integrations
        └── irflow-integration-websvc

From here, move into your newly cloned repo, and run the following:

.. code-block:: shell

    $ ./setup_websvc.sh

Once the service has been setup once, it can be started and stopped on demand with the ``start_websvc.sh`` and
``stop_websvc.sh`` scripts respectively.

Setting up for Development
--------------------------

.. code-block:: shell

    $ pipenv install --dev --skip-lock


Setting up your environment
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Pipenv supports the use of ``.env`` files. If your development configuration is unusual, you may need to provide default
values for environment variables that are different from the assumed defaults. At minimum, a debug variable should be
set when developing so that flask will provide debug information in-browser should an exception be hit:

.. code-block:: shell

    INTEGRATIONS_DEBUG=TRUE

The above line should be place in a file named ``.env`` (with no prefix before the ``.``), which should be located in
the root of the repository.

Running the webservice
^^^^^^^^^^^^^^^^^^^^^^

Using pipenv, you can drop into a subshell within the pipenv-created environment by running

.. code-block:: shell

    $ pipenv shell

Single commands can be run in the environment (without creating a subshell) with

.. code-block:: shell

    $ pipenv run <command>

Once in the environment, the webservice can be run as follows

.. code-block:: shell

    $ ./wsgi.py




.. _Pipenv: https://pipenv.readthedocs.io/en/latest/