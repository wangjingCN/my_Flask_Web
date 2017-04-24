#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import render_template
from . import main
from flask_login import login_required


@main.route('/', methods=['GET', 'POST'])
@login_required
def index():
    return render_template('index_new.html')
    # 需要写一个装饰器，判断是否登录，如果登录了，则跳到index,并生成对应的menu
