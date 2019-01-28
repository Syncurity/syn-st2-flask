""" Simple Static File Server for use with IR-Flow and the IR-Flow Integrations Framework """
from flask import Flask, send_from_directory
import os

from integrations_websvc import config

app = Flask(__name__)

app.config.from_object(config)
if os.path.exists(os.path.join(os.getcwd(), 'config.py')):
    app.config.from_pyfile(os.path.join(os.getcwd(), 'config.py'))

app.secret_key = app.config['SECRET_KEY']

STATIC_FILES_PATH = app.config['BASE_PATH']


@app.route('/lists/<path:path>')
def get_list_at_path(path):
    print(STATIC_FILES_PATH)
    return send_from_directory(STATIC_FILES_PATH, path)
