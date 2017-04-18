#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import render_template, request, flash, redirect, url_for, abort, session,_request_ctx_stack
from . import auth
from ...models import User


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.form and request.form['userName'] and request.form['password']:
        if request.form['userName'] == 'x':
            flash("invlad username")
            return redirect(url_for('.login'))
        session['current_user'] = request.form['userName']
        user=request.form['userName']
        if user:
            print user
            _request_ctx_stack.top.user = user
        return redirect(request.args.get('next') or url_for('main.index'))
        user = User.query.filter_by(username=request.form['userName'])
        if user and user.verify_password(request.form['password']):
            pass
        flash('invald username or password')

    # if form.validate_on_submit():
    #     user = User.query.filter_by(email=form.email.data).first()
    #     if user is not None and user.verify_password(form.password.data):
    #         login_user(user, form.remember_me.data)
    #         return redirect(request.args.get('next') or url_for('main.index'))
    #     flash('Invalid username or password.')
    return render_template('auth/login.html')


@auth.route('/logout')
# @login_required
def logout():
    # logout_user()
    # flash('You have been logged out.')
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
