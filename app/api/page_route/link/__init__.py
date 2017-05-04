#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Blueprint, render_template

link = Blueprint('link', __name__)


@link.route('/link')
def link_index():
    return render_template("meizi/meizi.html", title=u'精彩的妹子图片')
