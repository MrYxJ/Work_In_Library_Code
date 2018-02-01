#!/usr/bin/env python
#coding:utf-8
#url :http://fz.people.com.cn/skygb/sk/index.php/Index/seach
import bs4
import requests
from rule_ye import  GetHTMLText
from New_Work.new_rule_ye import Crawler
from bs4 import BeautifulSoup

import re
class cralwer(Crawler):
    URL = 'http://www.letpub.com.cn/index.php?page=grant&currentpage='
    URL_LAST = '&name=&person=&no=&company=&startTime=2017&endTime=2017&money1=0&money2=100000000&subcategory=&addcomment_s1=0&addcomment_s2=0&addcomment_s3=0#fundlisttable'

    def find_all_url(self,url):
        headers = {

        }
        data = 'pageIndex=0&pageSize=20&cgly=&hy=&cgDQ=&year=2017%2C2016&cgmc=%25&cgdywcdw=&wcr=&cgkeyword=&type=&lxname=&lxcode=&starttime=&endtime='

        ulist = []
        html = requests.post()

    def parse_body(self,url):
        total_ans= []
        html = GetHTMLText(url)
        soup = BeautifulSoup(html,"lxml")
        trs = soup.select('.table_yjfx')[0].find_all('tr')
        cnt = (len(trs) -3)/3
        for i in range(2,len(trs)-3,3):
            ans = {
                'Pno': '',  # 批准号
                'Ptitle': '',  # 项目名称
                'Pclassify': '',  # 项目类别
                'Ano': '',  # 申请代码
                'Response': '',  # 项目负责人
                'Party': '',  # 项目参与者
                'Organiza': '',  # 单位
                'Time': '',  # 立项时间
                'Funds': '',  # 资助经费
                'Year': '',  # 资助年度
                'AbstractCN': '',  # 中文摘要
                'AbstractEN': '',  # 英文摘要
                'KeyEN': '',  # 英文关键词
                'Summary': '',  # 结题摘要
                'Report': '',  # 结题报告
                'ResponseLink': '',  # 项目负责人链接
                'OrganizaLink': '',  # 单位链接
                'Result': '',  # 项目成果
                'Begindata': '',  # 开始时间
                'Enddata': '',  # 借宿时间
                'Prostate': '',  # 项目状态
                'Fund': '',  # 基金类型
                'Source': '',  # 基金来源
                'Sourceclass': '',  # 来源类别
                'Area': '',  # 研究方向（领域，学科）
                'Term': '',  # 期限
                'Nation': '',  # 国别
                'Url': ''  # url
            }
            tds = trs[i].find_all('td')
            ans['Response'] = tds[0].text
            ans['Organiza'] = tds[1].text
            ans['Funds'] = tds[2].text
            ans['Pno'] = tds[3].text
            ans['Pclassify'] = tds[4].text
            ans['Time'] = tds[6].text
            tds = trs[i+1].find_all('td')
            ans['Ptitle'] =tds[1].text
            tds = trs[i+2].find_all('td')
            ans['Area'] = tds[1].text
            total_ans.append(ans)
        return  total_ans

    def solve(self,ulist = None):
        ulist = cra.find_all_url(self.URL, 2054,self.URL_LAST)
        conlist = []
        for index,url in enumerate(ulist):
            print(index,':',url)
            conlist.extend(self.parse_body(url))
        return conlist

if __name__ == '__main__':
     cra = cralwer()
     #cra.solve()
     url = 'http://www.letpub.com.cn/index.php?page=grant&currentpage=1&name=&person=&no=&company=&startTime=2017&endTime=2017&money1=0&money2=100000000&subcategory=&addcomment_s1=0&addcomment_s2=0&addcomment_s3=0#fundlisttable'
     for line in cra.solve():
         print(line)
