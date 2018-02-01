#!/usr/bin/env python
#coding:utf-8
#url :http://fz.people.com.cn/skygb/sk/index.php/Index/seach
import bs4
from rule_ye import  GetHTMLText
from New_Work.new_rule_ye import Crawler
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from rule_ye import  clean_word_scriptstyle
import re
import requests

headers = {
    'Host': 'm.weibo.cn',
    'Referer': 'https://m.weibo.cn/u/2830678474',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
}

class cralwer(Crawler):
    URL = "http://or.nsfc.gov.cn/"

    def clean_word(self,sstr):  # 消除一段话中所有转义符号
        return " ".join(sstr.split())

    def find_all_url(self,url):
        cnt = 0
        ulist = []
        while True:
            print('url', url + str(cnt))
            soup = BeautifulSoup(GetHTMLText(url + str(cnt)), 'lxml')
            items = soup.select('.item')
            for item in items:
                divs = item('div')
                Time = str(divs[3].string)
                Str = str(divs[1].find('a')['href'])
                url_str = urljoin(self.URL, Str)
                Time = Time[1:-1]
                if Time != "2017":
                    return ulist
                else:
                    ulist.append(url_str)
            cnt += 100

    def get_content(self,row):
        return self.clean_word(row.select('.col-2')[0].text)

    def parse_body(self,url):
        html = GetHTMLText(url)
        soup = BeautifulSoup(html,"lxml").select('#item-right')[0]
        conlist = []
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
        rows = soup.select('.row')
        for row in rows:
            name = row.select('.col-1')[0].text
            if name == "Author":  ans['Party'] = self.get_content(row)
            elif name == "Date Issued" : ans['Time'] = self.get_content(row)
            elif name == "Keywords": ans['KeyEN'] = self.get_content(row)
            elif name == "English Abstract": ans['AbstractEN'] = self.get_content(row)
            elif name == "Program" : ans['Fund'] = self.get_content(row)
            elif name == "Project ID": ans['Pno'] = self.get_content(row)
            elif name == "Sponsorship": ans['Ptitle'] = self.get_content(row)
            elif name == "Institution": ans['Organiza'] = self.get_content(row)
            elif name == "Subject" : ans['Area'] = self.get_content(row)
            ans['Url'] = url
            ans['Nation'] = '中国'
            ans['Result'] = self.clean_word(soup.select('.main-title')[0].text)
        #print('rows',rows)
        #ans['Party'] = soup.find_all(text='作者').parent
        #print(soup.find(text='直接质谱分析纳升级复杂样品的基础研究'))
        # ans['Time'] = self.clean_word(rows[2].find(attrs={'class':'col-2'}).text)
        # ans['Fund'] = self.clean_word(rows[3].find(attrs={'class':'col-2'}).text)
        # ans['Pno'] = self.clean_word(rows[4].find(attrs={'class':'col-2'}).text)
        # ans['Ptitle'] = self.clean_word(rows[5].find(attrs={'class': 'col-2'}).text)
        # ans['Organiza'] = self.clean_word(rows[6].find(attrs={'class':'col-2'}).text)
        # ans['Area'] = self.clean_word(rows[9].find(attrs={'class':'col-2'}).text)
        # ans['Url'] = url
        # ans['Result'] = self.clean_word(soup.select('.main-title')[0].text)
        # ans['Nation'] = '中国'
        #print(ans.values())
        return tuple(ans.values())

    def solve(self,ulist = None):
        url = 'http://or.nsfc.gov.cn/nsfc-search?query=&sort_by=dc.date.issued_dt&order=desc&rpp=100&etal=0&start='
        ulist = self.find_all_url(url)
        conlist = []
        for index,url in enumerate(ulist):
            print(index,':',url)
            conlist.append(self.parse_body(url))
        return conlist


if __name__ == '__main__':
    cra = cralwer()
    cra.write_to_dbms('or_nsfc_gov_cn')
    print('Successful !!!!!!!')
    #url ='http://or.nsfc.gov.cn/handle/00001903-5/345845'
    #print(cra.parse_body(url))