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

def StringToDict(s, sep='+', kvSep='^'):
    if s[0] == sep:
	s = s[1:]
    if s[-1] == sep:
	s = s[0:-1]

    ret = dict()
    parts = s.split(sep)
    for p in parts:
	kv = p.split(kvSep)
	if len(kv) != 2: # 字符串格式有问题
	    return None
	ret[kv[0]] = kv[1]
    return ret
