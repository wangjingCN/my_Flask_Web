#!/usr/bin/env python
# -*- coding:UTF-8 -*-
from flask import Flask
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy

from config import config
from loggingHelper import getLogger

bcrypt = Bcrypt()
# from flask_admin import Admin

db = SQLAlchemy()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    db.init_app(app)
    bcrypt.init_app(app)

    from api.main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    
    return app
    # from app.upload import main as main_blueprint
    # app.register_blueprint(main_blueprint)
    #
    # from app.upload import create_admin_page
    # create_admin_page(app)
    # return app
