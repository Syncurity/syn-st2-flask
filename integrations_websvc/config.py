import secrets
import os
from os import environ as env

APP_NAME='irflow_integrations_websvc'
DEBUG = True if env.get('INTEGRATIONS_DEBUG', 'false').lower() == 'true' else False
IP = env.get('INTEGRATIONS_WEBSVC_IP', '0.0.0.0')
PORT = env.get('INTEGRATIONS_WEBSVC_PORT', 8080)
SECRET_KEY = env.get('INTEGRATIONS_WEBSVC_SECRET_KEY', default=''.join(secrets.token_hex(16)))
BASE_PATH = env.get('INTEGRATIONS_WEBSVC_BASE_PATH', os.path.abspath('integrations_websvc/static/'))
