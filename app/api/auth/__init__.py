#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Blueprint, render_template
from flask_restful import Api
from auth import AuthClass

auth = Blueprint('auth', __name__)
auth_api = Api(auth)
auth_api.add_resource(AuthClass, '/auth/get_token')

from . import views
