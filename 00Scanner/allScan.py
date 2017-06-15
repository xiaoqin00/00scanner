#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by xiaoqin00 on 2017/5/10

import mainSpider
import webManagerScan
from weakPassCracker import weakPassCracker as weakPassCracker
from subDomainsBrute import subDomainsBrute as subDomainBrute
import portScan.allPortsScan.allportsScan as allPortScan
#findshell不在综合之列
import cmsScan.cmsScan as cmsScan
import cPartAndWebPrintsScan.httpscan as cpart
import socket

def main(target):
    print 'spider run--------------------------------------------------'
    mainSpider.main(target)
    print 'webmanager run--------------------------------------------------'
    webManagerScan.main(target)
    print 'cpart run--------------------------------------------------'
    target=target[9:]
    print target
    try:
        result = socket.getaddrinfo(target, None)
        return result[0][4][0]
    except:
        return 0
    print result
    cpart.main(result)
    print 'portsScan run--------------------------------------------------'
    allPortScan.main(target)
    # print 'webpasscracker run-------------------------------------------------#-'
    # weakPassCracker.main(target)
    # print 'subdomain run------------------------------------------------#--'
    # tmp=target[9:]
    # subDomainBrute.main(tmp)
    # print 'cmsscan run--------------------------------------------------#'
    # cmsScan.main(target)

main('http://www.wenlong.date')

