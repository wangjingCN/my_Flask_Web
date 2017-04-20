#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import render_template, request, flash, redirect, url_for, abort, session, g
from . import auth
from ...models import User


@auth.before_app_request
def init_data():
    pass


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.form and request.form['userName'] and request.form['password']:
        user = User.query.filter_by(username=request.form['userName']).first()
        # if not user or not user.verify_password(request.form['password']):
        if not user:
            flash("invlad username")
            return redirect(url_for('.login'))
        session['current_user'] = user.username
        return redirect(request.args.get('next') or url_for('main.index'))
    return render_template('auth/login.html')


@auth.route('/logout')
# @login_required
def logout():
    # logout_user()
    # flash('You have been logged out.')
    session.pop("current_user", None)
    return redirect(url_for('main.index'))


@auth.route('/register', methods=['GET', 'POST'])
def register():
    # form = RegistrationForm()
    # if form.validate_on_submit():
    #     user = User(email=form.email.data,
    #                 username=form.username.data,
    #                 password=form.password.data)
    #     db.session.add(user)
    #     db.session.commit()
    #     token = user.generate_confirmation_token()
    #     send_email(user.email, 'Confirm Your Account',
    #                'auth/email/confirm', user=user, token=token)
    #     flash('A confirmation email has been sent to you by email.')
    #     return redirect(url_for('auth.login'))
    return render_template('auth/register.html')
