"""
Simple Webservice to serve text files for dynamic lists et. al
"""
import os

from flask import Flask, send_from_directory

app = Flask('irflow_integration_websvc')

BASE_PATH = os.environ.get('EDL_PATH')


@app.route('/edl/<path:path>')
def serve_files(path):
    return send_from_directory('static', path)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8081)
