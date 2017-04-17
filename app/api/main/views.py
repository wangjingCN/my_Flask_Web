#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import render_template
from . import main


@main.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index_new.html')
