#!/usr/bin/env python
import os
from app import create_app, db
from app.models import DBNSZone, DBNSDevice, DBNSLink, DBNSNSIPAssign, DBSYSDevice, DBSYSMenu, DBSYSUser, \
    DBSYSUserMapMenu
from flask.ext.script import Manager, Shell
from flask.ext.migrate import Migrate, MigrateCommand

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)
migrate = Migrate(app, db)


def make_shell_context():
    return dict(app=app, db=db, DBNSZone=DBNSZone,
                DBNSDevice=DBNSDevice, DBNSLink=DBNSLink, DBNSNSIPAssign=DBNSNSIPAssign, DBSYSDevice=DBSYSDevice,DBSYSUserMapMenu=DBSYSUserMapMenu
                )


manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)


@manager.command
def test():
    """Run the unit tests."""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)


@manager.option('-d', '-drop_first', dest='drop_first', default=False)
def createdb(drop_first):
    """Creates the database."""
    if drop_first:
        print 1
        db.drop_all()
    db.create_all()

@manager.command
def yes(name="Fred"):
    print "hello", name


if __name__ == '__main__':
    manager.run()
