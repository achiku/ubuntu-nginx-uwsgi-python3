# -*- coding: utf-8 -*-
from flask import Blueprint, jsonify

from .model import db

bp = Blueprint(
    'api', __name__, url_prefix='/api/v1')


@bp.route('/hello', methods=['GET'])
def hello():
    """say hello"""
    time = db.session.query('now()').scalar()
    result = {
        'greeting': 'hello',
        'time': time,
    }
    return jsonify(result)
