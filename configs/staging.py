# -*- coding: utf-8 -*-
import os

from configs.common import *  # NOQA

DEBUG = True
TESTING = True
SECRET_KEY = 'jFzUvndNIofD7kNTmJIPlYY5GnIuYXXPCenv72GEgfbCQDheBY'
ENVIRONMENT = 'staging'

DB_HOST = os.getenv('DB_HOST')
DB_NAME = os.getenv('DB_NAME')
DB_USER = os.getenv('DB_USER')
DB_PASS = os.getenv('DB_PASS')
SQLALCHEMY_DATABASE_URI = 'postgresql://{0}:{1}@{2}/{3}'.format(DB_USER, DB_PASS, DB_HOST, DB_NAME)
