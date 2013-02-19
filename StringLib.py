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

def StepSepString(s, sep, step):
    i = 0
    sio = StringIO()
    while i + step < len(s):
	sio.write(s[i:i+step])
	sio.write(sep)
	i = i + step
    sio.write(s[i:i+step])
    return sio.getvalue()


def __main():
    print('%s' % (StepSepString('834f9c861a9e', ':', 2)))
    print('%s' % (StepSepString('834f9c861a9', ':', 2)))
    print('%s' % (StepSepString('8', ':', 2)))


if __name__ == '__main__':
    __main()
