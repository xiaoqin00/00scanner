# -*- coding:utf8 -*-
# !/usr/bin/python
# Python:     2.7.8
# Platform:    Windows
# Program:     端口扫描
# History:     2015.6.1

import socket, time, thread,os

socket.setdefaulttimeout(3)


def socket_port(ip, port):
    """
    输入IP和端口号，扫描判断端口是否开放
    """
    try:
        if port >= 65535:
            print u'端口扫描结束'
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = s.connect_ex((ip, port))
        if result == 0:
            # print 'test2'
            lock.acquire()
            print ip, u':', port, u'端口开放'
            try:
                print port
                sqlAdd = 'insert into portsscan(port)VALUES ("%s;")' % port
                cursor.execute(sqlAdd)
                db.commit()
            except Exception, e:
                print'2', e
            # try:
            #     f=open('./../../result/allPorts.txt','w')
            #     # print 'test'
            #     tmp=str(ip)+' '+str(port)
            #     f.write(tmp)
            #     f.close()
            # except Exception,e:
            #     print 'file open error:',e
            lock.release()
        s.close()
    except:
        print u'端口扫描异常'


def ip_scan(ip):
    """
    输入IP，扫描IP的0-65534端口情况
    """
    try:
        print u'开始扫描 %s' % ip
        start_time = time.time()
        for i in range(0, 65534):
            thread.start_new_thread(socket_port, (ip, int(i)))
        print u'扫描端口完成，总共用时 ：%.2f' % (time.time() - start_time)
        raw_input("Press Enter to Exit")
    except:
        print u'扫描ip出错'

import pymysql
#
# if __name__ == '__main__':
def main(url):
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
    #     os.remove('./../../result/allPorts.txt')
    # except Exception,e:
    #     print e
#     url = raw_input('Input the ip you want to scan:\n')
    lock = thread.allocate_lock()
    ip_scan(url)
    db.close()
    return

target='http://www.wenlong.date'
# target='8.8.8.8'
main(target)