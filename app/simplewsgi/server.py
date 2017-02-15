#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'wang jing'
from wsgiref.simple_server import make_server
from hello import application

httpd = make_server('', 580, application)
print 'server http on port 580'
httpd.serve_forever
