#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Blueprint, render_template

link = Blueprint('link', __name__)


@link.route('/link')
def link_index():
    return render_template("link/link.html", title=u"这个是我们的link")
