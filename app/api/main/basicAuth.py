#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask.ext.httpauth import HTTPBasicAuth
from flask import make_response, jsonify

auth = HTTPBasicAuth()


# api的用法：@auth.login_required

@auth.get_password
def get_password(username):
    if username == 'ok':
        return 'python'
    return None


@auth.error_handler
def unauthorized():
    return make_response(jsonify({'error': 'Unauthorized access'}), 401)
