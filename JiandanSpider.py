#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re, requests
#without threading

RequestsHeaders= {'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                   'Accept-Encoding':'gzip, deflate, sdch',
                   'Accept-Language':'zh-CN,zh;q=0.8',
                   'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.36'}

#requests
def gethtml(url, Ps4= False):
    htmlinfo= requests.get(url, headers= RequestsHeaders, stream= Ps4)
    return htmlinfo


#save picture
def savepic(picpath, picname, picinfo):
    with open(picpath+picname,'wb')as f:
        for i in picinfo.iter_content(chunk_size= 500000):
            if i:
                f.write(i)

def spiderman()
