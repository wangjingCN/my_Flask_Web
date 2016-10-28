#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from . import db
from sqlalchemy.exc import IntegrityError

db_ns_device_link = \
    db.Table("ns_device_link",
             db.Column('device_id', db.Integer, db.ForeignKey('ns_device.id')),
             db.Column('link_id', db.Integer, db.ForeignKey('ns_link.id')))


class BaseOperator(object):
    def save(self):
        db.session.add(self)
        try:
            db.session.commit()
        except IntegrityError:
            db.session.rollback()
        return self

    def update(self):
        try:
            db.session.commit()
        except IntegrityError:
            db.session.rollback()
        return self

    def delete(self):
        db.session.delete(self)
        try:
            db.session.commit()
        except IntegrityError:
            db.session.rollback()
        return self


class DBNSZone(db.Model,BaseOperator):
    __tablename__ = 'ns_zone'

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(255))
    displayName = db.Column(db.String(255))
    addressList = db.Column(db.Text())
    devices = db.relationship(
        'DBNSDevice',
        backref='ns_zone',
        lazy='subquery'
    )

    def __repr__(self):
        return self.displayName


class DBNSDevice(db.Model, BaseOperator):
    '''
    负载均衡变更中使用的设备组信息
    每个设备组可以关联多个已管理的设备
    '''
    __tablename__ = 'ns_device'

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(255))
    displayName = db.Column(db.String(255))
    zone_id = db.Column(db.Integer(), db.ForeignKey('ns_zone.id'))
    configFile = db.Column(db.Text())
    configTime = db.Column(db.DateTime())
    # deviceList = db.Column(db.String(255))
    persistProfileName = db.Column(db.String(255))
    links = db.relationship(
        'DBNSLink',
        secondary=db_ns_device_link,
        backref=db.backref('ns_devices', lazy='dynamic')
    )
    devices = db.relationship(
        'DBSYSDevice',
        backref='ns_device',
        lazy='subquery'
    )

    def __repr__(self):
        return self.displayName


class DBNSLink(db.Model):
    '''
    负载均衡变更中使用的链路信息
    '''
    __tablename__ = 'ns_link'

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(255))
    displayName = db.Column(db.String(255))
    addressList = db.Column(db.Text())

    def __repr__(self):
        return self.displayName


class DBNSNSIPAssign(db.Model):
    '''
    IP地址分配信息
    '''
    __tablename__ = 'ns_ip_assign'

    id = db.Column(db.Integer(), primary_key=True)


class DBSYSDevice(db.Model):
    '''
    定义自动化运维平台管理的所有系统，包括IP、用户、密码等信息
    '''
    __tablename__ = 'device'

    id = db.Column(db.Integer(), primary_key=True)
    user = db.Column(db.String(255))
    password = db.Column(db.String(255))
    enable_password = db.Column(db.String(255))
    device_ip = db.Column(db.String(255), primary_key=True)
    host_name = db.Column(db.String(255))
    device_port = db.Column(db.Integer())
    connection = db.Column(db.String(20))
    device = db.Column(db.String(20))
    name = db.Column(db.String(20))
    ns_device_id = db.Column(db.Integer(), db.ForeignKey('ns_device.id'))

    def __repr__(self):
        return self.name


class DBSYSMenu(db.Model):
    __tablename__ = 'menu'
    id = db.Column(db.Integer(), primary_key=True)
    sectionName = db.Column(db.String(255))
    sectionDesc = db.Column(db.String(255))
    parent_id = db.Column(db.Integer(), default=-1)
    sectionURL = db.Column(db.String(255))
    isLeaf = db.Column(db.Boolean(), default=False)
    level = db.Column(db.Integer(), default=1)
    menus = db.relationship(
        'DBSYSUserMapMenu',
        backref='menu',
        lazy='subquery'
    )

    def __repr__(self):
        return self.sectionDesc


class DBSYSUser(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer(), primary_key=True)
    userName = db.Column(db.String(255), unique=True, index=True)
    password = db.Column(db.String(255))
    users = db.relationship(
        'DBSYSUserMapMenu',
        backref='user',
        lazy='subquery'
    )

    def __repr__(self):
        return self.userName


class DBSYSUserMapMenu(db.Model,BaseOperator):
    __tablename__ = 'user_map_menu'
    id = db.Column(db.Integer(), primary_key=True)
    user_id = db.Column(db.Integer(), db.ForeignKey('user.id'))
    menu_id = db.Column(db.Integer(), db.ForeignKey('menu.id'))

