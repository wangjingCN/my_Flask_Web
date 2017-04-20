#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from . import db, bcrypt
from .commonUtil.aesHelper import prpcrypt


class User(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(120))  # 这个密码可以用来还原的,如果用bcrypt.generate_password_hash来生成密码,则是不能还原的

    def __init__(self, username="", password=""):
        self.username = username
        if password:
            self.set_password(password)
        else:
            self.password = None

    def set_password(self, password):
        self.password = bcrypt.generate_password_hash(password)
        # self.password = prpcrypt().encrypt(password)

    def check_password(self, value):
        return bcrypt.check_password_hash(self.password, value)

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return unicode(self.id)

    def __str__(self):
        return '<User %r>' % self.username

    __repr__ = __str__
    # s=Student(),repr方法是实例s调用这个主要是作为测试来调用,,str方法时类Student()调用
