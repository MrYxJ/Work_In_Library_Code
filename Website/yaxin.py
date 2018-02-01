#!/usr/bin/env python
#coding:utf-8

from urllib.request import urlopen
from urllib.error import HTTPError,URLError
from bs4 import BeautifulSoup
from urllib.parse import urljoin

import requests
import re
import hashlib
from rule import GetHTMLText,GetTitleUrl,GetContent,GetWebsite,GetKeyWords,GetImg2md5,GetClassify,GetDate,GetImgUrl,GetSource,GetTitle,GetUrl2md5
from rule import solution1
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) ' 'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36'
}

class yaxin :
    analyse_rule = {
        'GetTitle' : ['.htitle'],
        'GetDate' : ['#pubtime_baidu'],
        'GetSource' : ['#source_baidu'],
        'GetClassify' : ['.f14'],
        'GetContent': ['.article-detail'],
        'GetImgUrl' : ['.article-detail','.piccontext'],
        'GetWebsite' :['亚新新闻网'],
        'GetKeyWords':None
    }


if __name__ == '__main__':
    url = "http://www.iyaxin.com/content/201801/08/c202775.html"
    soup = BeautifulSoup(GetHTMLText(url),'html.parser')
    a = yaxin()
    #print(GetImgUrl(url,soup,a.analyse_rule['GetImgUrl']))
    print(solution1('123',url,a.analyse_rule))