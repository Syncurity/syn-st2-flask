from flask import Flask, send_from_directory
import os

app = Flask(__name__)

BASE_PATH = os.environ.get('EDL_PATH')


@app.route('/edl/<path:path>')
def serve_files(path):
    return send_from_directory('static', path)


if __name__ == '__main__':
    app.run()
