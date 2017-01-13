# -*- coding: utf-8 -*-
import os

from configs.common import *  # NOQA

DEBUG = False
TESTING = False
SECRET_KEY = 'ZwxZMJ10yVNInpnVaKYnmHh6qYumoSFV98h3kqGpsdfB1naoNN'
ENVIRONMENT = 'production'

DB_HOST = os.getenv('DB_HOST')
DB_NAME = os.getenv('DB_NAME')
DB_USER = os.getenv('DB_USER')
DB_PASS = os.getenv('DB_PASS')
SQLALCHEMY_DATABASE_URI = 'postgresql://{0}:{1}@{2}/{3}'.format(DB_USER, DB_PASS, DB_HOST, DB_NAME)
