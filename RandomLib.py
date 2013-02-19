#!/usr/bin/env python

try:
    from cStringIO import StringIO
except ImportError:
    from StringIO import StringIO

def RanNumberString(length, prefix=''):
    import random
    random.seed()
    sio = StringIO()   
    sio.write(prefix)
    for i in range(length-len(prefix)):
	sio.write(str(random.randint(0,9)))
    return sio.getvalue()

def RanMacString():
    import random
    import HexLib
    random.seed()
    sio = StringIO()
    for i in range(12):
	sio.write(HexLib.ToHexStr(random.randint(0,15)))
    return sio.getvalue()
