#!/usr/bin/env python
#coding:utf-8
#url :http://fz.people.com.cn/skygb/sk/index.php/Index/seach
import bs4
from rule_ye import  GetHTMLText
from New_Work.new_rule_ye import Crawler
from bs4 import BeautifulSoup
import re
set = {''}
class cralwer(Crawler):
    def find_all_url(self,url,cnt):
        ulist = []
        for i in range(cnt):
            ulist.append(url+str(i+1))
        return ulist

    def parse_body(self,url):
        html = GetHTMLText(url)
        soup = BeautifulSoup(html,"html.parser")
        conlist = []
        tbody = soup.select('.jc_a table')[0].find_all('tr')
        for tr in tbody[1:]:
             if isinstance(tr, bs4.element.Tag):
                 tds = tr('td')
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
                 ans['Pno'] = tds[0].string
                 ans['Pclassify'] = tds[1].string
                 ans['Area'] = tds[2].string
                 ans['Ptitle'] = tds[3].string
                 ans['Time'] = tds[4].string
                 ans['Response'] = tds[5].string
                 ans['Organiza'] = tds[7].string
                 ans['Nation'] = tds[9].string
                 ans['Result'] = tds[11].string
                 ans['Begindata'] = tds[14].string
                 ans['Url'] = url
                 if ans['Pno'] in set : continue
                 else : set.add(ans['Pno'])
                 conlist.append(tuple(ans.values()))
        return conlist

    def solve(self, ulist = None):
        url = 'http://fz.people.com.cn/skygb/sk/index.php/Index/seach?lxtime=2017&29lxtime=2017&p='
        ulist = self.find_all_url(url,291)
        conlist = []
        for index,url in enumerate(ulist):
            print(index,':',url)
            conlist.extend(self.parse_body(url))
        print(len(conlist))
        return conlist



if __name__ == '__main__':
    cra = cralwer()
    #cra.solve()
    cra.write_to_dbms('fz_people_com_cn')
    #for i in cra.parse_body('http://fz.people.com.cn/skygb/sk/index.php/Index/seach?lxtime=2017&1'):
    #    print(i)