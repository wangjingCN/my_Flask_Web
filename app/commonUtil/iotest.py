#!/usr/bin/env python
# -*- coding: utf-8 -*-
import codecs
import os
import json

print os.environ
print os.getenv('TMP')
try:
    import cPickle as pickle
except ImportError:
    import pickle

d = dict(name='wangjing')
print d
print pickle.dumps(d)
print pickle.loads(pickle.dumps(d))
print json.dumps(d)  # 把对象json化
__author__ = 'wang jing'
with codecs.open('imoc.txt', 'rb', 'utf-8') as f:
    for line in f.readlines():
        # print line.strip()
        pass
