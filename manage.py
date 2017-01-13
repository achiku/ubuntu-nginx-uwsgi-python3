# -*- coding: utf-8 -*-
from flask_script import Manager  # type: ignore

from app import create_app

config_file_path = '../configs/development.py'
manager = Manager(create_app(config_file_path))


if __name__ == "__main__":
    manager.run()
