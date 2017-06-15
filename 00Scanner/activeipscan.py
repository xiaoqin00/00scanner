#!/usr/bin/env python
# -*- coding: utf-8 -*-

import platform
import sys
import os
import time
import thread

def get_os():
    '''
    get os 类型
    '''
    os = platform.system()
    if os == "Windows":
        return "n"
    else:
        return "c"

def ping_ip(ip_str):
    cmd = ["ping", "-{op}".format(op=get_os()),
           "1", ip_str]
    output = os.popen(" ".join(cmd)).readlines()
    flag = False
    for line in list(output):
        if not line:
            continue
        if str(line).upper().find("TTL") >= 0:
            flag = True
            break
    if flag:
        print "ip: %s is ok ***" % ip_str

def find_ip(ip_prefix):
    '''
    给出当前的127.0.0 ，然后扫描整个段所有地址
    '''
    for i in range(1, 256):
        ip = '%s.%s' % (ip_prefix, i)
        thread.start_new_thread(ping_ip, (ip,))
        time.sleep(0.3)

def main(target):
    print "start time %s" % time.ctime()
    # commandargs = sys.argv[1:]
    commandargs = target
    args = "".join(commandargs)
    ip_prefix = '.'.join(args.split('.')[:-1])
    find_ip(ip_prefix)
    print "end time %s" % time.ctime()

# target='127.0.0.1'
# main(target)