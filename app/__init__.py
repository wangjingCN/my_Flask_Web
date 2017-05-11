#!/usr/bin/env python
# -*- coding:UTF-8 -*-
from flask import Flask
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

from config import config
from loggingHelper import getLogger
from flask_babelex import Babel

bcrypt = Bcrypt()

db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = "auth.login"
login_manager.session_protection = "strong"




def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)

    babel = Babel()
    babel.init_app(app)

    from api.main import main
    app.register_blueprint(main)

    from api.auth import auth
    app.register_blueprint(auth)

    from api.flask_admin import create_admin_page
    create_admin_page(app)

    from api.page_route import meinv, link
    app.register_blueprint(meinv)
    app.register_blueprint(link)

    return app
