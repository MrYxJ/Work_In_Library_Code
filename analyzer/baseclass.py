#!/usr/bin/env python
#coding:utf-8

class BaseClass():
    def __init__(self,url_md5,content,title_url):
        self.url_md5 =url_md5
        self.content = content
        self.title_url = title_url

    def analyze(self):
        title=date=source=classify=content=img_urls=img_md5= keywords= website=add_time=''
        item = (self.url_md5, title,  date, source, classify,content,
                img_urls, img_md5,self.title_url ,keywords,website, add_time)
        return item

