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
from rule import solution
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) ' 'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36'
}

class sanyard :
    analyse_rule = {
        'GetTitle' : '.list_2_-l44 h2',
        'GetDate' : '.pubtime',
        'GetSource' : '三亚新闻网',
        'GetClassify' : '.list_2_l11',
        'GetContent': '.list_2_l55',
        'GetImgUrl' : 'list_2_l55',
        'GetWebsite' : '三亚新闻网',
        'GetKeyWords':None
    }



if __name__ == '__main__':
    List = []
    print(List)
    if List: print('ok')
    else : print('No')
    url = "http://www.sanyarb.com.cn/content/2018-01/15/content_291892.htm"
    soup = BeautifulSoup(GetHTMLText(url), 'html.parser')
    #print(solution('1',url,'2',a.analyse_rule))
    print(GetContent(soup,'.list_2_l55',url))