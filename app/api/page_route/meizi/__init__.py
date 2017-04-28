#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Blueprint, render_template

meinv = Blueprint('meinv', __name__)


@meinv.route('/pic')
def meinv_pic():
    return render_template("meizi/meizi.html", title=u'精彩的妹子图片')
