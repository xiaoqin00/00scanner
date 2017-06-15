#encoding:gbk
import re
import os

def Check(filestr,filepath):

    #php zend一句话  caidao.php
    if filestr[:4]=='Zend':
        if os.path.getsize(filepath)==178:
            return (('Zend Encode',),),'zend加密php一句话后门'

        #其他后门判断c
        return None
