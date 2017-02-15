#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'wang jing'

from flask import Flask,render_template
from flask import request

app = Flask(__name__)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.form['username'] == 'username':
        return '<h3>Hello, admin!</h3>'
    return render_template('index_new.html')


def application(environ, start_response):
    method = environ['REQUEST_METHOD']
    path = environ['PATH_INFO']
    if method == 'GET' and path == '/login':
        pass
        # return handle_home(environ, start_response)
    return ['<h1>Hello, web!</h1>']


if __name__ == "__main__":
    app.run()
