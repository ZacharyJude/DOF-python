#!/usr/bin/env python
# -*- coding:utf-8 -*-

def IPv4ToInt(ipv4):
    parts = ipv4.split('.')
    if len(parts) != 4:
	return False
    ret = 0
    ret = ret + (int(parts[3]))
    ret = ret + (int(parts[2]) << 8)
    ret = ret + (int(parts[1]) << 16)
    ret = ret + (int(parts[0]) << 24)
    return ret


def __TestIPv4ToInt():
    print('123.456.23.1 to int: %d' % (IPv4ToInt('123.456.23.1')))

if __name__ == '__main__':
    __TestIPv4ToInt()
