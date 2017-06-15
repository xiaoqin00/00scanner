#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by xiaoqin00 on 2017/5/1
from threading import *
from socket import *
import os
import pymysql

screenLock = Semaphore(value=1)
port = [21, 22, 23, 25, 53, 80, 389, 8080, 1433,
        2375, 3306, 3389, 6379, 11211, 27017]


def connScan(tgtHost, tgtPort):

    try:
        connSkt = socket(AF_INET, SOCK_STREAM)
        connSkt.connect((tgtHost, tgtPort))
        # establishes a connection to target
        connSkt.send('PythonPortScan\r\n')
        # send a string of data to the open port and wait for the response,如果没成功就报错
        results = connSkt.recv(100)  # the response might give us an indication of the appliction running on the target host and port
        screenLock.acquire()
        port=str(tgtPort)
        try:
            print port
            sqlAdd='insert into portsscan(port)VALUES ("%s;")'%port
            cursor.execute(sqlAdd)
            db.commit()
        except Exception,e:
            print'2',e
        tmp='[+]%d/tcp open' % tgtPort +'[+] ' + str(results)
        # f=open('./../../result/partPorts.txt','w')
        # f.write(tmp)
        # f.close()
        return '[+]%d/tcp open' % tgtPort +'[+] ' + str(results)
    except:
        screenLock.acquire()
        tmp='[-]%d/tcp closed' % tgtPort
        # f = open('./../../result/partPorts.txt', 'w')
        # f.write(tmp)
        # f.close()
        return '[-]%d/tcp closed' % tgtPort
    finally:
        screenLock.release()
        connSkt.close()


def portScan(tgtHost):
    global db,cursor
    try:
        db=pymysql.connect('localhost','root','root','test')
        cursor=db.cursor()
        sqlDelete='delete from portsscan'
        cursor.execute(sqlDelete)
        db.commit()
    except Exception,e:
        print '1',e
    # try:
    #     os.remove('./../../result/partPorts.txt')
    # except Exception,e:
    #     print e
    '''try:
        tgtName=gethostbyaddr(tgtIP)
        print '\n[+] Scan results for:
'+tgtName[0]
    except:
        print 'Scan Results for: '+ tgtIP'''
    setdefaulttimeout(1)
    ports = []
    tgtHost = tgtHost.strip('http:').strip('/')
    for tgtPort in port:
        i = connScan(tgtHost, int(tgtPort))
        ports.append(i)
    db.close()
    return ports


print portScan('http://www.wenlong.date')