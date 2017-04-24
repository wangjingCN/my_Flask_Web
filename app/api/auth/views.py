#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import render_template, request, flash, redirect, url_for, session
from . import auth
from ...models import User
from flask_login import login_user, logout_user, login_required


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.form and request.form['userName'] and request.form['password']:
        user = User.query.filter_by(username=request.form['userName']).first()
        if user and user.check_password(request.form['password']):
            login_user(user, remember=request.form['remember'])
            return redirect(request.args.get('next') or url_for('main.index'))
        flash('Invalid username or password.')
        return redirect(url_for('.login'))
    return render_template('auth/login.html')


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.')
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
