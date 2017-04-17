from flask import Blueprint, render_template

main = Blueprint('main', __name__)


# from . import views, errors
@main.app_errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@main.app_errorhandler(500)
def internal_server_error(e):
    return render_template('errpage/500.html'), 500
