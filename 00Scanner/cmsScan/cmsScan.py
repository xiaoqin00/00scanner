#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by xiaoqin00 on 2017/5/7
from threading import Thread
import sys,urllib2,json,utils,time,socket,glob,threading,os,random
from multiprocessing import Pool
from hashlib import md5
import requests


def connection(tmptarget):
    mark = ''
    try:
        response = urllib2.urlopen(tmptarget)
        if response:
            mark = 1
        response.close()
    except:
        mark = 0
    return mark
import pymysql
def main(target):
    print 'cmsScan running'
    try:
        db=pymysql.connect('localhost','root','root','test')
        cursor=db.cursor()
    except Exception,e:
        print '1',e
    sqlDelete='delete from cmsscan'
    try:
        cursor.execute(sqlDelete)
        db.commit()
    except Exception,e:
        print '2',e
    cms_quan=[]
    cms = glob.glob('Bin\*.txt')
    print 'wenjian num: {}'.format(len(cms)),'wenjian:',cms
    for i in cms:
        cms_url=[cms_url.rstrip() for cms_url in open(i)]
        print i
        print 'url',cms_url
        for u in cms_url:
            u=u.split('-----')[0]
            tmptarget=target+u
            print tmptarget
            if connection(tmptarget):
                print i, u
                try:
                    tmp=i
                    tmp=tmp[4:-4]
                    tmp=str(tmp)
                    print tmp
                    sqlAdd='insert into cmsscan(cmsscan)VALUES ("%s")'%tmp
                    try:
                        cursor.execute(sqlAdd)
                        db.commit()
                        db.close()
                    except Exception,e:
                        print '3',e
                except Exception,e:
                    print '4',                                                          e
                return
                # break
            else:
                continue
    db.close()


target='http://www.wenlong.date'
main(target)