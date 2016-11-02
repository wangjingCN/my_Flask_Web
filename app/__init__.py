#!/usr/bin/env python
# -*- coding:UTF-8 -*-
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from config import config
from .loggingHelper import logger,log_file_folder

db = SQLAlchemy()
# bootstrap = Bootstrap()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    db.init_app(app)
    return app


