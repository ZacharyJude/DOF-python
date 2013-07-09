#! /usr/bin/env python
# -*- coding:utf-8 -*-

import os, sys
import os.path as osp
import urllib2 as ul2
import urllib as ul
import httplib
import socket
import cookielib
import Cookie
import re
import types
import codecs
import time

LOCAL_CONFIG = dict()
LOCAL_CONFIG['HTTP_FETCH_INTERVAL_SEC'] = 2




class HttpFetcher:
    def __init__(self, cookieFileName=None, autoSaveCookie=False):
	self.__cookieFileName = cookieFileName
	self.__autoSaveCookie = autoSaveCookie
	pass




    def FetchPage(self, url, data=None, referer=None, userAgent=None, rawCookieHeader=None):
		return self.Fetch(url, data, referer, userAgent, rawCookieHeader)




	def Fetch(self, url, data=None, referer=None, userAgent=None, rawCookieHeader=None):
	"""Fetch a page of given url
	 @param[in] url: fetch target url. type str
	 @return response object, call read() can get the html content of the target page. (False, msg)--exception
	"""
	try:
	    loginCookieJar = None
	    if None != self.__cookieFileName:
		# if cookie is needed
		loginCookieJar = cookielib.MozillaCookieJar();
		loginCookieJar.load(self.__cookieFileName, True, True)
		opener = ul2.build_opener(ul2.HTTPCookieProcessor(loginCookieJar))
	    else:
		# no cookie needed
		opener = ul2.build_opener()

	    for i in range(len(opener.addheaders)):
		print(opener.addheaders[i])

	    if None != userAgent:
		for i in range(len(opener.addheaders)):
		    # opener.addheaders[i] is header
		    if 'user-agent' == opener.addheaders[i][0].lower():
			opener.addheaders[i] = ('User-agent', userAgent)
			break

	    if None != referer:
		opener.addheaders.append(('Referer', referer))

	    if None != rawCookieHeader:
		opener.addheaders.append(('Cookie', rawCookieHeader))

	    rep = opener.open(url, data);

	    if None != loginCookieJar and True == self.__autoSaveCookie:
		loginCookieJar.save(self.__cookieFileName, True, True)

	    takeRestTimeSec = LOCAL_CONFIG['HTTP_FETCH_INTERVAL_SEC']
	    if takeRestTimeSec > 0:
		time.sleep(takeRestTimeSec)

	    return rep
	except socket.error as inst:
	    print 'socket error occurs when fetching page:%s' % str(inst)
	    return False
	except ul2.URLError as inst:
	    print 'url error occurs when fetching page:%s' % str(inst)
	    return False
	except httplib.IncompleteRead as inst:
	    print 'incomplete read error occurs when fetching page:%s' % str(inst)
	    return False
	except ul2.HttpError as inst:
	    print'http error occurs when fetching page:%s' % str(inst)
	except Exception as inst:
	    print 'unknown exception occurs when fetching page:%s' % str(inst)
	    return False





class PostDataBuilder:
    def __init__(self):
	self.__dataHolder = dict()





    def AddData(self, key, value):
	if type('') != type(key) or None == key:
	    raise

	self.__dataHolder[key] = value





    def Build(self):
	return ul.urlencode(self.__dataHolder)




    def Clear(self):
	self.__dataHolder.clear()
