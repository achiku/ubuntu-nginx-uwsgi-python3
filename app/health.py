# -*- coding: utf-8 -*-
from flask import Blueprint, jsonify

from .model import db

bp = Blueprint(
    'healthcheck', __name__, url_prefix='/healthcheck')


@bp.route('/', methods=['GET'])
def index():
    """Healthcheck"""
    cnt = db.session.query('now()').scalar()
    result = ['ok: {0}'.format(cnt)]
    return jsonify(result)
