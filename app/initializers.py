# -*- coding: utf-8 -*-

from .model import db
from .api import bp as app_api
from .health import bp as app_health


def database(app):
    """init DB"""
    db.init_app(app)
    return app


def blueprint(app):
    """ init Blueprint """
    app.register_blueprint(app_api)
    app.register_blueprint(app_health)
    return app
