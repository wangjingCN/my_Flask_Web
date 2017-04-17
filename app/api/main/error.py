#!/usr/bin/env python
# -*- coding: utf-8 -*-
from . import main
from flask import render_template


@main.app_errorhandler(404)
def page_not_found(e):
    return render_template('errpage/404.html'), 404


@main.app_errorhandler(500)
def page_not_found(e):
    return render_template('errpage/500.html'), 500
