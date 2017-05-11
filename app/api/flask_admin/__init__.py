#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask_admin import Admin, BaseView, expose, AdminIndexView
from flask_admin.contrib.sqla import ModelView
from app.models import User
from app import db
from wtforms import PasswordField
from flask_login import current_user

# admin_page = Admin(name=u'基础配置', index_view=AdminIndexView(name=u"导航栏", url='/admin'), template_mode='bootstrap3')
admin_page = Admin(name=u'基础配置', template_mode='bootstrap3')


class MyView(ModelView):
    def is_accessible(self):
        if current_user.is_authenticated and current_user.username == "root":
            return True
        return False


# class DBNSDeviceModelView(ModelView):
#     # column_exclude_list = ['name', 'displayName', 'configTime', 'persistProfileName', 'zone', ]
#     column_select_related_list = DBNSDevice.zone_id
#     page_size = 20

class UserView(MyView):
    # form_excluded_columns = ('password')
    form_extra_fields = {
        'setPassword': PasswordField('newpassword')
    }
    # set the form fields to use
    form_columns = (
        'username',
        'password',
        'setPassword'
    )

    def on_model_change(self, form, User, is_created):  # password加密时bcrypt的写法
        # def on_model_change(self, form, User):
        if form.setPassword.data is not None:
            User.set_password(form.setPassword.data)
            # del form.password

    def on_form_prefill(self, form, id):
        # form.password.data = ''
        pass

    column_filters = ('username', 'password')
# class MyView(BaseView):
#     @expose('/')
#     def index(self):
#         return self.render('deviceEdit.html')


def create_admin_page(app):
    admin_page.init_app(app)
    admin_page.add_view(UserView(User, db.session, name=u"用户"))
    # admin_page.add_view(MyView(name=u'设备信息'))
    # admin_page.add_view(MyView(name='Hello 3',endpoint='test3', category=u'设备信息'))
