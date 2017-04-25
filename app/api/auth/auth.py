#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask_restful import Resource, reqparse
from ...models import User
from itsdangerous import TimedJSONWebSignatureSerializer
from flask import current_app,abort

user_auth_token_post = reqparse.RequestParser()
user_auth_token_post.add_argument('username', type=str, required=True, trim=True)
user_auth_token_post.add_argument('password', type=str, required=True, trim=True)


class AuthClass(Resource):
    def get(self):
        args = user_auth_token_post.parse_args()
        user = User.query.filter_by(username=args['username']).first()
        if user and user.check_password(args['password']):
            s = TimedJSONWebSignatureSerializer(current_app.config['SECRET_KEY'], expires_in=600)
            return {'token': s.dumps({"id": user.id})}
        else:
            abort(401)
