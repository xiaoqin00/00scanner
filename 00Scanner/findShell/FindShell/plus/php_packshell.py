#!/usr/bin/python2.7
#coding:gbk

import re

rule='gzdeflate|gzcompress|gzencode'


#此插件白名单列表 (['文件路径'],['误报特征码'])
whitefilter=[]


def Check(filestr,filepath):

    result = re.search(rule,filestr)

    try:
        if result.group():
            if '打包' in filestr and 'unix2DosTime' in filestr:
                isok = 1
                for white in whitefilter:
                    if white[0][0] in filepath.replace('\\','/') and white[1][0] in key:
                        isok=0
                if isok:
                    return (('暂不提供',),),'PHP 文件打包后门程序'
    except:
        pass
    return None
