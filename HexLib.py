#!/usr/bin/env python

try:
    from cStringIO import StringIO
except ImportError:
    from StringIO import StringIO

def ToHexStr(s):
    if type('') == type(s):
	sio = StringIO()
	for c in s:
	    h = hex(0xFF & ord(c)).replace('0x', '')
	    if len(h) == 1:
		sio.write('0')
	    sio.write(h)
	return sio.getvalue()


    if type(0) == type(s):
	return hex(s).replace('0x', '')

    if type(bytearray()) == type(s):
	sio = StringIO()
	for b in s:
	    h = hex(0xFF & b).replace('0x', '')
	    if len(h) == 1:
		sio.write('0')
	    sio.write(h)
	return sio.getvalue()

def ToByteArray(v, padding=None, isReverse=False):
    b = bytearray()
    while v != 0:
	b.append(0xFF & v)
	v = v >> 8
    if None != padding:
	remain = len(b) % padding
	for i in range(remain):
	    b.append(0xFF & 0)
    if isReverse:
	b.reverse()
    return b
