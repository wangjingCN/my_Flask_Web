#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import render_template
from . import main


@main.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')
    # return app.send_static_file('index.html') #不经过渲染直接输出html