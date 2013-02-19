def RamNumberString(length, prefix=''):
    import random
    random.seed()
    sio = StringIO()   
    sio.write(prefix)
    for i in range(length-len(prefix)):
	sio.write(str(random.randint(0,9)))
    return sio.getvalue()

def RamMacString():
    import random
    import HexLib
    random.seed()
    sio = StringIO()
    for i in range(12):
	sio.write(ToHexStr(random.randint(0,16)))
    return sio.getvalue()
