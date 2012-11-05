#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os, sys, os.path
try:
    from cStringIO import StringIO
except ImportError:
    from StringIO import StringIO

def CollectionToString(col, sep='+', isWithLeadingSep=False):
    sio = StringIO()
    if True == isWithLeadingSep:
	sio.write(sep)

    size = len(col)
    cnt = 1 
    for x in col:
	sio.write(x)
	if cnt < size:
	    sio.write(sep)

	cnt = cnt + 1 

    return sio.getvalue()
