#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re, requests, os
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


#get 无聊图图片(picinfolist用来收集信息，最后返回这个列表，这么做不为别的，就是想调试时候方便点)
def spiderman(page):
        url= 'http://jandan.net/pic/page-'+str(page)
        picinfolist = []
        if os.path.exists(str(page)):
            pass
        else:
            os.makedirs(str(page))
#以页码为名称，创建文件夹

        htmlinfo = gethtml(url)
        piclist = re.findall('查看原图.*"(.*[jpgnif]{3})"', htmlinfo.text)
#获取目标图片地址的列表

        for picinfo in piclist:
            if picinfo[:2]== '//':
                picinfo = 'http:'+picinfo
            if os.name == 'nt':
                picpath = '.\\'+str(page)+'\\'
            else:
                picpath = './'+str(page)+'/'
            picname = os.path.split(picinfo)[1]
            htmlinfo= gethtml(picinfo,True)
            picinfolist.append([picpath,picname,htmlinfo])
        return picinfolist
#get picpath, pathname, pathinfo and so on

if __name__ == '__main__':
    while True:
        num = input('请输入页码范围，min-max，请输入数字，中间用-隔开,退出输入“q”：')
        if num == 'Q':
            break
        min = int(num.split('-')[0])
        max = int(num.split('-')[1])+1
        for page in range(min, max):
            picinfolist = spiderman(page)
            for x in picinfolist:
                savepic(x[0],x[1],x[2])

