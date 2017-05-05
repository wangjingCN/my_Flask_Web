#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from . import db, bcrypt
from itsdangerous import TimedJSONWebSignatureSerializer, BadSignature, SignatureExpired
from . import login_manager
from flask import current_app
from datetime import datetime


class User(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(120))  # 这个密码可以用来还原的,如果用bcrypt.generate_password_hash来生成密码,则是不能还原的
    sex = db.Column(db.String(10))
    address = db.Column(db.String(255))  # 居住地
    work_address = db.Column(db.String(255))  # 工作地点
    birth = db.Column(db.DateTime, default=datetime.now())  # 出生日期
    year_money = db.Column(db.String(255))  # 年收入
    marital_status = db.Column(db.String(25))  # 婚姻状态 单身，热恋中，已婚
    requirement_opposite = db.Column(db.Text)  # 对异性的要求
    qq = db.Column(db.String(255))
    weixin = db.Column(db.String(255))  # 微信号
    tel = db.Column(db.String(255))  # 电话，唯一字段
    e_mail = db.Column(db.String(255))
    personal_detail = db.Column(db.Text)  # 个人情况说明,谈谈爱好，兴趣，工作内容，家庭状况
    pic_url = db.Column(db.String(255))  # 头像地址

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

    @staticmethod
    def verify_auth_token(token):
        s = TimedJSONWebSignatureSerializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except SignatureExpired:
            return None
        except BadSignature:
            return None
        user = User.query.get(data['id'])
        return user

    def __str__(self):
        return '<User %r>' % self.username

    __repr__ = __str__
    # s=Student(),repr方法是实例s调用这个主要是作为测试来调用,,str方法时类Student()调用


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
