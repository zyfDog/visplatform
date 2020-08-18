import os
import sys
from visplatform import app

SECRET_KEY = os.getenv('SECRET_KEY', 'secret string')
MONGODB_SETTINGS ={
    'db': 'vis',
    'host': '127.0.0.1',
    'port': 27017
}
CSRF_ENABLED = True
UPLOAD_FOLDER = 'visplatform/data'