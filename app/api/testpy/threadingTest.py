#!/usr/bin/env python
# -*- coding: utf-8 -*-
import threading
from time import sleep


class Move(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name
        # super.__init__(threading.Thread)

    def run(self):
        print "i'm moving the %s" % (self.name)
        sleep(4)


if __name__ == "__main__":
    t1 = Move("石头")
    t1.start()
    print t1.getName()
    print t1.daemon
    t2 = Move("石头1")
    t2.start()
    print "我搬完了"
