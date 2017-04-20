from functools import wraps
from flask import g, render_template, session


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not session['current_user']:
            return render_template('main.index')
        return f(*args, **kwargs)

    return decorated_function
