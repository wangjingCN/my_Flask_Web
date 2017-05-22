#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask_wtf import Form
from wtforms import StringField
import threadingTest
from time import ctime,sleep

def music(name):
    for i in range(2):
        print "i want to listoning music %s %s" % (name, ctime())
        sleep(4)


def move(name):
    for i in range(2):
        print "i want to move %s %s" % (name, ctime())
        sleep(4)


if __name__ == "__main__":
    print  0.06*2500
    threads = []
    t1 = threadingTest.Thread(target=music, args=(u"月光",))
    threads.append(t1)
    t2 = threadingTest.Thread(target=move, args=(u"跑步",))
    threads.append(t2)
    for t in threads:
        t.setDaemon(True)
        t.start()
    t.join()
    print "finshed %s" % (ctime())
