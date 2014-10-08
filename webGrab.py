#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import urllib2
import re

# get data from html, simple version
def getUrlRespHtmlSimple(url):
    req = urllib2.Request(url)
    resp = urllib2.urlopen(req)
    respHtml = resp.read()
    # because of Chinese characters，transcode gbk to utf-8
    respHtml = respHtml.decode('gbk').encode('utf-8')
    return respHtml

# get data from html
def getUrlRespHtml(url):
    # disguise as a browser
    heads = {'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 
            'Accept-Charset':'GB2312,utf-8;q=0.7,*;q=0.7', 
            'Accept-Language':'zh-cn,zh;q=0.5', 
            'Cache-Control':'max-age=0', 
            'Connection':'keep-alive', 
            'Host':'John', 
            'Keep-Alive':'115', 
            'Referer':url, 
            'User-Agent':'Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.14) Gecko/20110221 Ubuntu/10.10 (maverick) Firefox/3.6.14'}

    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor())
    urllib2.install_opener(opener) 
    req = urllib2.Request(url)
    opener.addheaders = heads.items()
    respHtml = opener.open(req).read()
    return respHtml.decode('gbk').encode('utf-8')
