#!/usr/bin/env python
# -*- coding:UTF-8 -*-
from functools import wraps
from flask import g, render_template, session, url_for, redirect, abort, request, jsonify
from flask_login import current_user



def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not current_user:
            return redirect(url_for('auth.login'))
        return f(*args, **kwargs)

    return decorated_function


def menu_permission_required():
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if str(request.endpoint).lower() not in [
                str(menu.url).lower() for menu in current_user.menus]:
                abort(403)
            return f(*args, **kwargs)

        return decorated_function

    return decorator


def api_permission_required():
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            api_url_from_menu = []
            for each_api_list in [menu.apis for menu in current_user.menus]:
                for each_api in each_api_list:
                    if each_api:
                        api_url_from_menu.append(
                            (str(
                                each_api.url).lower(), str(
                                each_api.method).lower()))

            api_url_from_user = [
                (str(
                    api.url).lower(), str(
                    api.method).lower()) for api in current_user.apis]

            if (str(request.endpoint).lower(), str(request.method).lower()
                ) not in list(set(api_url_from_menu + api_url_from_user)):
                abort(403)
            return f(*args, **kwargs)

        return decorated_function

    return decorator
