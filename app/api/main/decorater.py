from functools import wraps
from flask import g, render_template, session, url_for, redirect


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        # if not g.current_user:
        #     print "yyyy"
        if 'current_user' not in session:
            return redirect(url_for('auth.login'))
        return f(*args, **kwargs)

    return decorated_function
