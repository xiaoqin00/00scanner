#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by xiaoqin00 on 2017/5/2

import requests
import re
import pymysql
import sqlScan

def url_is_correct(url):
    global db
    global cursor
    # '''
    # 使用requests.get方法判断url是否正确,并返回url
    # :return:
    # '''
    try:
        print url
        #url = "http://10.70.18.47:8080" 这是我内网环境的测试地址
        requests.get(url)
        print('test',url,type(url))
        sql="insert into unvisitedurl(unvisitedurl)VALUES ('%s');"%url   #将我们输入的url检查后插入未访问表中
        print(sql)
        try:
            cursor.execute(sql)
            db.commit()
        except Exception as e:
            db.rollback()
            print('url_is_correct()--error',e)
        return url
    except Exception,e:
        print('please input the correct url!!!',e)
        #exit(-1)   #如果url是固定写入的，那么必须添加此句，否则会一直循环
    return url_is_correct(url)



def url_protocol(url):
    '''
    获取输入的url地址的协议，是http、https等
    '''
    print('the protocol of this site:' + re.findall(r'.*(?=://)',url)[0])
    return re.findall(r'.*(?=://)',url)[0]



def same_url(url):
    '''
    处理用户输入的url，并为后续判断是否为一个站点的url做准备，爬取的时候不能爬到其它站，那么爬取将无止境
    :return: sameurl
    '''
    #将完整的url中的http://删除
    url = url.replace(urlprotocol + '://','')
    #判断删除http://之后的url有没有www，如果没有就加上‘www.’，但不存储，
    #只是为了同化所有将要处理的url，都有了‘www.’之后，
    #就可以找以‘www.’开始的到第一个‘/’结束中的所有字符串作为该站的主域名
    if re.findall(r'^www',url) == []:
        sameurl = 'www.' + url
        if sameurl.find('/') != -1:
            sameurl = re.findall(r'(?<=www.).*?(?=/)', sameurl)[0]
        else:
            sameurl = sameurl + '/'
            sameurl = re.findall(r'(?<=www.).*?(?=/)', sameurl)[0]
    else:
        if url.find('/') != -1:
            sameurl = re.findall(r'(?<=www.).*?(?=/)', url)[0]
        else:
            sameurl = url + '/'
            sameurl = re.findall(r'(?<=www.).*?(?=/)', sameurl)[0]
    print('the same site URL:' + sameurl)
    return sameurl

class Spider():
    '''
    真正的爬取程序
    '''
    def __init__(self,url):
        self.current_deepth = 1    #设置爬取的深度
        self.url=url
        '''
        这里需要注意:
        爬取分为：***先深度后广度***和***先广度和后深度***
        1、如果是先深度后广度，那么给定一个url，然后从其页面中的任意一个可用链接进行深度爬取，很可能无限至循环下去
        （在处理不当的时候，但一般情况下大家都会处理的很好，无非是判断哪些url是已经爬取过的，哪些是新爬取到的url）
        2、如果是先广度后深度，就是将一个url页面中的所有链接进行爬取，然后分类处理过滤
        （在这种处理不当的时候也会出现无限循环的可能，但一般情况下大家都会处理的很好，无非是判断哪些url是已经爬取过的，哪些是新爬取到的url）
        '''
    def getPageLinks(self,url):
        '''
        获取页面中的所有链接
        '''
        pageSource = requests.get(self.url).text
        pageLinks = re.findall(r'(?<=href=\").*?(?=\")|(?<=href=\').*?(?=\')',pageSource)
        #self.page_links = self.page_links + pageLinks
        #print(self.page_links)
        for l in pageLinks:  #出去连接中的单引号
            tmp=l.split("'")
            print(tmp)
            l=tmp[0]
            print(l)
        for l in pageLinks:
            print(self.url + 'the url in this page:' + l)
        #for l in self.page_links:
        #    print(url + '该页面的源码链接有：' + l)
        #return self.page_links
        return pageLinks

    def processUrl(self,url):
        '''
        判断正确的链接及处理相对路径为正确的完整url
        :return:
        '''
        true_url = []
        for l in self.getPageLinks(url):
            if re.findall(r'/',l):
                if re.findall(r':',l):
                    true_url.append(l)
                else:
                    true_url.append(urlprotocol + '://' + domain_url + l)
        #print(trueUrl)
        for l in true_url:
            print(self.url + 'the useful url in this page:' + l)
        return true_url

    def sameTargetUrl(self,url):
        '''
        判断是否为同一站点链接，防止爬出站外，然后导致无限尝试爬取
        '''
        same_target_url = []
        for l in self.processUrl(url):
            if re.findall(domain_url,l):
                same_target_url.append(l)
        #print(self.same_target_url)
        for l in same_target_url:
            print(self.url + 'the same url in this page:' + l)
        return same_target_url

    def unrepectUrl(self,url):
        '''
        删除重复url
        '''
        unrepect_url = []
        for l in self.sameTargetUrl(url):
            if l not in unrepect_url:
                unrepect_url.append(l)
        for l in unrepect_url:
            print(self.url + 'the unique url in this page:' + l)
        #print(self.unrepect_url)
        return unrepect_url

    def crawler(self,crawl_deepth=1):
        visitedcheck=''
        '''
        正式的爬取，并依据深度进行爬取层级控制
        '''

        def checkunvisitedurl():  # 基于全站爬取
            unvisitedurlcheckemptysql = "select * from unvisitedurl limit 1"  # 检查未访问的url表
            try:
                cursor.execute(unvisitedurlcheckemptysql)
                result = cursor.fetchone()
            except Exception as e:
                print(e)
            return result

        while self.current_deepth <= crawl_deepth:   #基于深度爬取
            print('deeptest')
            while checkunvisitedurl():
                print('checktest')
                getunvisitedurlsql="select * from unvisitedurl limit 1"
                try:
                    cursor.execute(getunvisitedurlsql)
                    visitingurl=cursor.fetchone()
                except Exception as e:
                    print('getunvisitedurlsql--error!',e)
                print 'visitingurl:',visitingurl,type(visitingurl)
                visitingurl=visitingurl[0]
                links=self.unrepectUrl(visitingurl)   #最开始的url由用户输入，后面就从数据库读取
                print '!!!!!!!!!!!',visitingurl
                if not visitingurl.split('/')[-1].find('css'):
                    result=sqlScan.main(visitingurl)   #如果有sql注入，就向漏洞库中插入数据
                    if result:

                        sql_vul='insert into sqlscan(sqlscan)VALUES ("%s")'%visitingurl
                        try:
                            vul_cursor.execute(sql_vul)
                            vul_db.commit()
                        except Exception,e:
                            print 'vul_sql--error!',e

                # getunvisitedurlsql="select * from unvisitedurl limit 1"
                # try:
                #     cursor.execute(getunvisitedurlsql)
                #     url=cursor.fetchone()
                # except Exception as e:
                #     print('getunvisitedurlsql--error!',e)
                # print(url)
                delunvisitedsql="delete from unvisitedurl where unvisitedurl='%s'"%visitingurl   #将访问了的页面从未访问页面中删除
                print(delunvisitedsql)
                try:
                    print('delunvisitedsql')
                    cursor.execute(delunvisitedsql)
                    db.commit()
                except Exception as e:
                    db.rollback()
                    print('delunvisitedsql--error!',e)
                insertvisitedurlsql="insert into visitedurl(visitedurl)VALUES ('%s');"%visitingurl  #将已经访问了的页面存入访问页面中
                print(insertvisitedurlsql)
                try:
                    print('insertvisitedurlsql')
                    cursor.execute(insertvisitedurlsql)
                    db.commit()
                except Exception as e:
                    db.rollback()
                    print('insertvisitedurlsql--error!',e)
                for link in links:
                    tmp=link.split("'")
                    link=tmp[0]
                    checkvisitedurlsql="""select * from visitedurl where visitedurl='%s';"""%link  #检查从当前页面爬来的域名是否已访问
                    print(checkvisitedurlsql)
                    try:
                        print('checkvisitedsql')
                        cursor.execute(checkvisitedurlsql)
                        visitedcheck=cursor.fetchone()
                    except Exception as e:
                        print('visitedcheck--error!',e)
                    if not visitedcheck:    #如果爬取的url没有访问过，检查后，那就将url存入未访问列表中
                        isexistinunvisitedsql="select * from unvisitedurl where unvisitedurl='%s'"%link   #检查unvisitedurl中是否已经有了
                        print(isexistinunvisitedsql)
                        try:
                            print('isexistinunvisitedsql')
                            cursor.execute(isexistinunvisitedsql)
                            isexistinunvisited=cursor.fetchone()
                        except Exception as e:
                            print('isexistinunvisitedsql--error!',e)
                        if not isexistinunvisited:  #如果爬去
                            insertunvisitedurlsql="""insert into unvisitedurl(unvisitedurl)VALUES ('%s');"""%link
                            print(insertunvisitedurlsql)

                            try:
                                print('insertunvisitedurlsql')
                                cursor.execute(insertunvisitedurlsql)
                                db.commit()
                            except Exception as e:
                                db.rollback()
                                print('insertunvisitedurlsql--error!',e)
            if not checkunvisitedurl():
                return 0
            self.current_deepth+=1

# if __name__ == '__main__':
def main(target):
    #删除原始表中的数据
    global db
    global cursor
    global urlprotocol
    global domain_url
    global vul_cursor
    global vul_db
    try:
        db = pymysql.connect('localhost', 'root', 'root', 'test')
        cursor = db.cursor()
    except Exception as e:
        print (e)
        exit()
    delvisiteddatasql="delete from visitedurl;"
    delunvisiteddatasql="delete from unvisitedurl;"
    try:
        cursor.execute(delunvisiteddatasql)
        cursor.execute(delvisiteddatasql)
        db.commit()
    except Exception as e:
        db.rollback()
        print(e)
    print('test')

    try:
        vul_db=pymysql.connect('localhost','root','root','test')
        vul_cursor=vul_db.cursor()
    except Exception,e:
        print 'vul_db--error!',e
    url = url_is_correct(target)  # 将验证为正确的url地址赋值给url
    urlprotocol = url_protocol(url)
    domain_url = same_url(url)

    spider = Spider(url)
    spider.crawler(100)
    db.close()

target='http://www.wenlong.date'
main(target)