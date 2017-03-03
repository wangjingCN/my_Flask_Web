#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'wang jing'
import re

m = re.search('(?<=abc)def', 'abcdef')
print m.group(0)
