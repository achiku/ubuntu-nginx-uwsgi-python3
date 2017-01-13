# -*- coding: utf-8
from flask import Flask  # type: ignore
from . import initializers


def create_app(config=None):
    """ Application Factories
        http://flask.pocoo.org/docs/patterns/appfactories/
    """
    app = Flask(
        __name__, static_folder='static/dist', static_url_path='/static')
    if config:
        app.config.from_pyfile(config)
    else:
        app.config.from_envvar('APP_CONFIG')

    initializers.blueprint(app)
    initializers.database(app)

    return app
