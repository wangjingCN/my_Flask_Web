#!/usr/bin/env python
# -*- coding:UTF-8 -*-
from flask import Flask
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

from config import config
from loggingHelper import getLogger

bcrypt = Bcrypt()
# from flask_admin import Admin

db = SQLAlchemy()
loginmanager = LoginManager()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    db.init_app(app)
    bcrypt.init_app(app)
    loginmanager.init_app(app)

    from api.main import main
    app.register_blueprint(main)

    from api.auth import auth
    app.register_blueprint(auth)

    return app
