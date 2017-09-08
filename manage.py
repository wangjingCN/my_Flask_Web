#!/usr/bin/env python
# -*- coding:UTF-8 -*-
import os
from app import create_app, db
from app.models import User
from flask_script import Manager, Shell
from flask_migrate import Migrate, MigrateCommand

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)
migrate = Migrate(app, db)


def make_shell_context():
    return dict(app=app, db=db, User=User)


manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)


@manager.command
def api():
    """Run the unit tests."""
    import unittest
    test = unittest.TestLoader().discover('test')
    unittest.TextTestRunner(verbosity=2).run(test)


@manager.option('-d', '-drop_first', dest='drop_first', default=False)
def createdb(drop_first):
    """Creates the database."""
    if drop_first:
        print 1
        db.drop_all()
    db.create_all()


if __name__ == '__main__':
    manager.run(default_command='runserver')
