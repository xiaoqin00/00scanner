#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by xiaoqin00 on 2017/5/2

from django.http import HttpResponse
from django.shortcuts import  render
import pymysql

def index(request):
     return render(request,'index.html',context=None)

def base(request):
     return render(request,'base.html',context=None)
def baseAction(request):
     import allScan
     target=request.GET['target']
     allScan.main(target)
     try:
          db=pymysql.connect('localhost','root','root','test')
          cursor=db.cursor()
          sqlcms='select * from cmsscan'
          cursor.execute(sqlcms)
          tmp1=cursor.fetchall()
          sqlcpart='select * from cpart'
          cursor.execute(sqlcpart)
          tmp2=cursor.fetchall()
          sqlfindshell='select * from findshell'
          cursor.execute(sqlfindshell)
          tmp3=cursor.fetchall()
          sqlportscan='select * from portsscan'
          cursor.execute(sqlportscan)
          tmp4=cursor.fetchall()
          sqlsql='select * from sqlscan '
          cursor.execute(sqlsql)
          tmp5=cursor.fetchall()
          sqlsubdomain='select * from subdoamin'
          cursor.execute(sqlsubdomain)
          tmp6=cursor.fetchall()
          sqlsitemap='select * from visitedurl'
          cursor.execute(sqlsitemap)
          tmp7=cursor.fetchall()
          sqlweakpass='select * from weakpass'
          cursor.execute(sqlweakpass)
          tmp8=cursor.fetchall()
          sqlwebmanager='select * from webmanager'
          cursor.execute(sqlwebmanager)
          tmp9=cursor.fetchall()
     except Exception,e:
          print e
     ttmp = ''
     ttmp = ttmp + '<h1>cms扫描</br></h1>'
     for i in tmp1:
          ttmp = '<h2>' + ttmp + str(i) + '</br></h2>'
     ttmp = ttmp + '<h1>c段和系统指纹扫描</br></h1>'
     for i in tmp2:
          print i
          ttmp = '<h2>' + ttmp + str(i) + '</br></h2>'
     ttmp = ttmp + '<h1>webshell扫描</br></h1>'
     for i in tmp3:
          print i
          ttmp = '<h2>' + ttmp + str(i) + '</br></h2>'
     ttmp = ttmp + '<h1>端口扫描</br></h1>'
     for i in tmp4:
          print i
          ttmp = '<h2>' + ttmp + str(i) + '</br><h2>'
     ttmp = ttmp + '<h1>sql扫描</br></h1>'
     for i in tmp5:
          print i
          ttmp = '<h2>' + ttmp + str(i) + '</br></h2>'
     ttmp = ttmp + '<h1>子域名扫描</br></h1>'
     for i in tmp6:
          print i
          ttmp = '<h2>' + ttmp + str(i) + '</br></h2>'
     ttmp = ttmp + '<h1>网站目录扫描</br></h1>'
     for i in tmp7:
          print i
          ttmp = '<h2>' + ttmp + str(i) + '</br></h2>'
     ttmp = ttmp + '<h1>弱口令扫描</br></h1>'
     for i in tmp8:
          print i
          ttmp = '<h2>' + ttmp + str(i) + '</br></h2>'
     ttmp = ttmp + '<h1>网站后台扫描</br></h1>'
     for i in tmp9:
          print i
          ttmp = '<h2>' + ttmp + str(i) + '</br></h2>'
     ttmp=ttmp.replace("'",'')
     ttmp=ttmp.replace(",",'')
     ttmp=ttmp.replace("(",'')
     ttmp=ttmp.replace(")",'')
     message = ttmp
     # message='cms扫描结果：'+tmp1+'\n'+'c段和系统指纹识别扫描结果：'+tmp2+'\n'+'webshell扫描结果：'+tmp3+'\n'+'端口扫描结果：'+tmp4+'\n'+'sql扫描结果：'+tmp5+'\n'+'子域名扫描结果：'+tmp6+'\n'+'网站目录扫描结果：'+tmp7+'\n'+'弱口令扫描结果：'+tmp8+'\n'+'后台扫描结果：'+tmp9+'\n'
     db.close()
     return HttpResponse(message)

def view(request):
     # try:
     db = pymysql.connect('localhost', 'root', 'root', 'test')
     cursor = db.cursor()
     sqlcms = 'select * from cmsscan'
     cursor.execute(sqlcms)
     tmp1= cursor.fetchall()
     sqlcpart = 'select * from cpart'
     cursor.execute(sqlcpart)
     tmp2= cursor.fetchall()
     sqlfindshell = 'select * from findshell'
     cursor.execute(sqlfindshell)
     tmp3= cursor.fetchall()
     sqlportscan = 'select * from portsscan'
     cursor.execute(sqlportscan)
     tmp4= cursor.fetchall()
     sqlsql = 'select * from sqlscan '
     cursor.execute(sqlsql)
     tmp5=  cursor.fetchall()
     sqlsubdomain = 'select * from subdomain'
     cursor.execute(sqlsubdomain)
     tmp6= cursor.fetchall()
     sqlsitemap = 'select * from visitedurl'
     cursor.execute(sqlsitemap)
     tmp7= cursor.fetchall()
     sqlweakpass = 'select * from weakpass'
     cursor.execute(sqlweakpass)
     tmp8=cursor.fetchall()
     sqlwebmanager = 'select * from webmanager'
     cursor.execute(sqlwebmanager)
     tmp9= cursor.fetchall()

     # except Exception, e:
     #      print e
     ttmp=''
     ttmp=ttmp+'<h1>cms扫描</br></h1>'
     for i in tmp1:
          ttmp='<h2>'+ttmp+str(i)+'</br></h2>'
     ttmp=ttmp+'<h1>c段和系统指纹扫描</br></h1>'
     for i in tmp2:
          print i
          ttmp='<h2>'+ttmp+str(i)+'</br></h2>'
     ttmp=ttmp+'<h1>webshell扫描</br></h1>'
     for i in tmp3:
          print i
          ttmp='<h2>'+ttmp+str(i)+'</br></h2>'
     ttmp=ttmp+'<h1>端口扫描</br></h1>'
     for i in tmp4:
          print i
          ttmp='<h2>'+ttmp+str(i)+'</br><h2>'
     ttmp = ttmp + '<h1>sql扫描</br></h1>'
     for i in tmp5:
          print i
          ttmp='<h2>'+ttmp+str(i)+'</br></h2>'
     ttmp = ttmp + '<h1>子域名扫描</br></h1>'
     for i in tmp6:
          print i
          ttmp='<h2>'+ttmp+str(i)+'</br></h2>'
     ttmp = ttmp + '<h1>网站目录扫描</br></h1>'
     for i in tmp7:
          print i
          ttmp='<h2>'+ttmp+str(i)+'</br></h2>'
     ttmp = ttmp + '<h1>弱口令扫描</br></h1>'
     for i in tmp8:
          print i
          ttmp='<h2>'+ttmp+str(i)+'</br></h2>'
     ttmp = ttmp + '<h1>网站后台扫描</br></h1>'
     for i in tmp9:
          print i
          ttmp='<h2>'+ttmp+str(i)+'</br></h2>'
     ttmp=ttmp.replace("'",'')
     ttmp=ttmp.replace(",",'')
     ttmp=ttmp.replace("(",'')
     ttmp=ttmp.replace(")",'')
     message=ttmp

     # message = 'cms扫描结果：' + tmp1 + '\n' + 'c段和系统指纹识别扫描结果：' + tmp2 + '\n' + 'webshell扫描结果：' + tmp3 + '\n' + '端口扫描结果：' + tmp4 + '\n' + 'sql扫描结果：' + tmp5 + '\n' + '子域名扫描结果：' + tmp6 + '\n' + '网站目录扫描结果：' + tmp7 + '\n' + '弱口令扫描结果：' + tmp8 + '\n' + '后台扫描结果：' + tmp9 + '\n'
     db.close()
     return HttpResponse(message)

def sqlScan(request):
     return render(request,'sqlScan.html',context=None)
def sqlScanAction(request):
     import sqlScan
     target=request.GET['target']
     sqlScan.main(target)
     try:
          db=pymysql.connect('localhost','root','root','test')
          cursor=db.cursor()
          sqlsql='select * from sqlscan'
          cursor.execute(sqlsql)
          tmp=cursor.fetchall()
     except Exception,e:
          print 'sqlscanAction--error!',e
     ttmp=''
     ttmp = ttmp + '<h1>sql扫描</br></h1>'
     for i in tmp:
          print i
          ttmp='<h2>'+ttmp+str(i)+'</br></h2>'
     ttmp = ttmp.replace("'", '')
     ttmp = ttmp.replace(",", '')
     ttmp = ttmp.replace("(", '')
     ttmp = ttmp.replace(")", '')
     message=ttmp
     db.close()
     return HttpResponse(message)

def webManagerScan(request):
     return render(request,'webManagerScan.html',context=None)
def webManagerScanAction(request):
     import webManagerScan
     target=request.GET['target']
     webManagerScan.main(target)
     try:
          db=pymysql.connect('localhost','root','root','test')
          cursor=db.cursor()
          sqlwebmanager='select * from webmanager'
          cursor.execute(sqlwebmanager)
          tmp=cursor.fetchall()
     except Exception,e:
          print 'webmanager--error',e

     ttmp = ''
     ttmp = ttmp + '<h1>网站后台扫描</br></h1>'
     for i in tmp:
          print i
          ttmp = '<h2>' + ttmp + str(i) + '</br></h2>'
     ttmp = ttmp.replace("'", '')
     ttmp = ttmp.replace(",", '')
     ttmp = ttmp.replace("(", '')
     ttmp = ttmp.replace(")", '')
     message = ttmp
     db.close()
     return HttpResponse(message)

def weakPassScan(request):
     return render(request,'weakPassScan.html',context=None)
def weakPassScanAction(request):
     import weakPassCracker.weakPassCracker as weakPassCracker
     target=request.GET['target']
     print target
     target=str(target)
     weakPassCracker.main(target)
     try:
          db=pymysql.connect('localhost','root','root','test')
          cursor=db.cursor()
          sqlweakpass='select * from weakpass'
          cursor.execute(sqlweakpass)
          tmp=cursor.fetchall()
          db.close()
          ttmp = ''
          ttmp = ttmp + '<h1>弱口令扫描</br></h1>'
          for i in tmp:
               print i
               ttmp = '<h2>' + ttmp + str(i) + '</br></h2>'
          ttmp = ttmp.replace("'", '')
          ttmp = ttmp.replace(",", '')
          ttmp = ttmp.replace("(", '')
          ttmp = ttmp.replace(")", '')
          message = ttmp
     except Exception,e:
          print e
     return HttpResponse(message)

def cmsScan(request):
     return  render(request,'cmsScan.html',context=None)
def cmsScanAction(request):
     import cmsScan.cmsScan as cmsScan
     target = request.GET['target']
     try:
          cmsScan.main(target)
          print 'cmsscan is run'
     except Exception,e:
          print e


     print target
     cmsScan.main(target)
     try:
          db=pymysql.connect('localhost','root','root','test')
          cursor=db.cursor()
          sqlcmsscan='select * from cmsscan'
          cursor.execute(sqlcmsscan)
          tmp=cursor.fetchall()
     except Exception,e:
          print e
     ttmp = ''
     ttmp = ttmp + '<h1>cms扫描</br></h1>'
     for i in tmp:
          print i
          ttmp = '<h2>' + ttmp + str(i) + '</br></h2>'
     ttmp = ttmp.replace("'", '')
     ttmp = ttmp.replace(",", '')
     ttmp = ttmp.replace("(", '')
     ttmp = ttmp.replace(")", '')
     message = ttmp
     db.close()
     print message
     return HttpResponse(message)

def cPartScan(request):
     return render(request,'cPartScan.html',context=None)
def cPartScanAction(request):
     import cPartAndWebPrintsScan.httpscan as cpart
     target=request.GET['target']
     target=str(target)
     import socket
     # target = target[9:]
     print target
     # try:
     #      result = socket.getaddrinfo(target, None)
     #      return result[0][4][0]
     # except:
     #      return 0
     # print result
     # cpart.main(target)
     try:
          db=pymysql.connect('localhost','root','root','test')
          cursor=db.cursor()
          sqlcpart='select * from cpart'
          cursor.execute(sqlcpart)
          tmp=cursor.fetchall()
     except Exception,e:
          print 'cpart--error!',e
     ttmp = ''
     ttmp = ttmp + '<h1>c段及系统指纹扫描</br></h1>'
     for i in tmp:
          print i
          ttmp = '<h2>' + ttmp + str(i) + '</br></h2>'
     ttmp=ttmp.replace("'",'')
     ttmp=ttmp.replace(",",'')
     ttmp=ttmp.replace("(",'')
     ttmp=ttmp.replace(")",'')
     message = ttmp
     # tmp1=''
     # for i in tmp:
     #      tmp1+=i
     # message =tmp1
     print 'tmp',tmp
     print 'message:',message

     db.close()
     return HttpResponse(message)

def findShell(request):
     return render(request,'findShell.html',context=None)
def findShellAction(request):
     import findShell.FindShell.main as findshell
     target=request.GET['target']
     findshell.main(target)
     try:
          db=pymysql.connect('localhost','root','root','test')
          cursor=db.cursor()
          sqlfindshell='select * from findshell'
          cursor.execute(sqlfindshell)
          tmp=cursor.fetchall()
     except Exception,e:
          print 'findshell--error!',e
     ttmp = ''
     ttmp = ttmp + '<h1>webshell扫描</br></h1>'
     for i in tmp:
          print i
          ttmp = '<h2>' + ttmp + str(i) + '</br></h2>'
     ttmp=ttmp.replace("'",'')
     ttmp=ttmp.replace(",",'')
     ttmp=ttmp.replace("(",'')
     ttmp=ttmp.replace(")",'')
     message = ttmp
     db.close()
     return HttpResponse(message)

def portScan(request):
     return render(request,'portScan.html',context=None)
def portScanAction(request):
     import partPortsScan
     target=request.GET['target']
     partPortsScan.portScan(target)
     # portScan..portScan(target)
     try:
          db=pymysql.connect('localhost','root','root','test')
          cursor=db.cursor()
          sqlportscan='select * from portsscan'
          cursor.execute(sqlportscan)
          tmp=cursor.fetchall()
     except Exception,e:
          print 'portsscan--error!',e
     ttmp = ''
     ttmp = ttmp + '<h1>端口扫描</br></h1>'
     for i in tmp:
          print i
          ttmp = '<h2>' + ttmp + str(i) + '</br></h2>'
     ttmp=ttmp.replace("'",'')
     ttmp=ttmp.replace(",",'')
     ttmp=ttmp.replace("(",'')
     ttmp=ttmp.replace(")",'')
     message = ttmp
     db.close()
     return HttpResponse(message)

def siteMapScan(request):
     return render(request,'siteMapScan.html',context=None)
def siteMapScanAction(request):
     import mainSpider
     target=request.GET['target']
     mainSpider.main(target)
     try:
          db=pymysql.connect('localhost','root','root','test')
          cursor=db.cursor()
          sqlsitemap='select * from visitedurl'
          cursor.execute(sqlsitemap)
          tmp=cursor.fetchall()
     except Exception,e:
          print 'sitemap--error',e
     ttmp = ''
     ttmp = ttmp + '<h1>网站目录扫描</br></h1>'
     for i in tmp:
          print i
          ttmp = '<h2>' + ttmp + str(i) + '</br></h2>'
     ttmp=ttmp.replace("'",'')
     ttmp=ttmp.replace(",",'')
     ttmp=ttmp.replace("(",'')
     ttmp=ttmp.replace(")",'')
     message = ttmp
     db.close()
     return HttpResponse(message)

def subDomainScan(request):
     return render(request,'subDomainScan.html',context=None)
def subDomainScanAction(request):
     # from . import subDomainsBrute
     import subDomainsBrute.subDomainsBrute as subdomain
     target=request.GET['target']
     subdomain.main(target)
     # subDomainsBrute.main(target)
     try:
          db=pymysql.connect('localhost','root','root','test')
          cursor=db.cursor()
          sqlsubdomain='select * from subdomain'
          cursor.execute(sqlsubdomain)
          tmp=cursor.fetchall()
     except Exception,e:
          print 'subdomain--error!',e
     ttmp = ''
     ttmp = ttmp + '<h1>子域名扫描</br></h1>'
     for i in tmp:
          print i
          ttmp = '<h2>' + ttmp + str(i) + '</br></h2>'
     ttmp=ttmp.replace("'",'')
     ttmp=ttmp.replace(",",'')
     ttmp=ttmp.replace("(",'')
     ttmp=ttmp.replace(")",'')
     message = ttmp
     db.close()
     return HttpResponse(message)

def test(request):
     return render(request,'test.html',context=None)
def test1():
     global test
     f=open('./result/test.txt','r')
     test=f.read()
     print test
def test2():
     test1()

message1='''<!DOCTYPE html>
<html>
	<head>
	    <title>AZScanner</title>
	    <link rel = "stylesheet" type = "text/css" href = "/static/css/style.css">
	    <link rel = "stylesheet" type = "text/css" href = "/static/css/bootstrap.css">
	    <link rel = "stylesheet" href = "/static/css/font-awesome.css">
	    <link rel = "stylesheet" type = "text/css" href = "/static/css/style.css">
	    <link rel = "stylesheet" href = "/static/css/animate.css">
	</head>
	<body >
	    <header class="navbar navbar-static-top bs-docs-nav" id="top" role="banner">
		  <div class="container">
		    <div class="navbar-header">
		      <button class="navbar-toggle collapsed" type="button" data-toggle="collapse" data-target="#bs-navbar" aria-controls="bs-navbar" aria-expanded="false">
		        <span class="sr-only">Toggle navigation</span>
		        <span class="icon-bar"></span>
		        <span class="icon-bar"></span>
		        <span class="icon-bar"></span>
		      </button>
		      <a href="" class="navbar-brand" onclick="window.history.go(-1)">返回任务列表</a>
		    </div>
		    <nav id="bs-navbar" class="collapse navbar-collapse">
				<ul class="nav navbar-nav navbar-right">
					<li>
					  	<a href="/index">AZScanner</a>
					</li>
					<li>
					  	<a href="/manager">任务</a>
					</li>
					<li>
					  	<a href="/manager">注入检测调度管理</a>
					</li>
				</ul>
		    </nav>
		  </div>
		</header>

		<div class="bs-docs-header" id="content" tabindex="-1">
	      <div class="container">
	        <h1 class="text-center">注入检测结果</h1>
	        <p class="lead">
		      	<a href="/manager" class="btn btn-outline-inverse btn-lg trace-btn">项目列表</a>
		      	<a href="/manager" class="btn btn-outline-inverse btn-lg trace-btn">注入检测管理</a>
		    </p>
	      </div>
	    </div>
	    <div class="container">
			<ul class="list-group">
				<li class="list-group-item active">注入检测结果</li>
					<div class="alert alert-success">{{id}}</div>
					<div class="alert alert-success">{{log}}</div>
					<div class="alert alert-success">{{data}}</div>

			</ul>
	    </div>


	</body>
	<script type = "text/javascript" src="/static/js/jquery-2.0.3.min.js"> </script>
	<script type = "text/javascript" src="/static/js/bootstrap.js"></script>
	<script type = "text/javascript" src="/static/js/Chart.min.js"></script>
	<script type="text/javascript">


	</script>
</html>'''