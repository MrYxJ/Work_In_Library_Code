#!/usr/bin/env python
#coding:utf-8
#url :http://fz.people.com.cn/skygb/sk/index.php/Index/seach
import bs4
from rule_ye import  GetHTMLText
from New_Work.new_rule_ye import Crawler
from bs4 import BeautifulSoup
from time import sleep
import re
from New_Work.Tool import write
from urllib.parse import urljoin

class cralwer(Crawler):
    URL = 'http://jjj.ci.cqvip.com/zk/search.aspx?page='
    URL_LAST = '&rf=YY%3D2017-2017&ls=0&so=2#search-result-list'
    error_url = []
    def find_all_url(self,url,cnt,url_last):
        ulist = []
        for i in range(cnt):
            url = url+str(i+1)+url_last
            soup = BeautifulSoup(GetHTMLText(url),'lxml')
            dls = soup.select('.search-result-list.abstract-list dl')
            for dl in dls:
                a = dl.select('.title.btnTitle')[0]
                ulist.append(urljoin('http://jjj.ci.cqvip.com',a['href']))
        return ulist

    def parse_body(self,url):
        html = GetHTMLText(url)
        if html == None :
            print('None url；',url)
            self.error_url.append(url)
            return None
        soup = BeautifulSoup(html,"lxml")
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
        ans
        return  tuple(ans.value)

    def solve(self,ulist = None,dbms_name = None):
        print('ok？')
        if ulist == None: ulist = cra.find_all_url(self.URL,199833,self.URL_LAST)
        conlist = []
        cnt = 0
        total_cnt =0
        for index,url in enumerate(ulist):
            tmp = self.parse_body(url)
            if tmp == None :continue
            conlist.extend(tmp)
            cnt += 1
            print('cnt:', cnt, ':url', url)
            if cnt == 50:
                total_cnt += cnt
                self.write_to_dbms(table_name=dbms_name, datas=conlist)
                print('Successful Write %s lines to %s totally writed % lines' % (cnt, dbms_name, total_cnt))
                cnt = 0
                conlist.clear()
        if len(conlist) != 0:
            total_cnt += cnt
            self.write_to_dbms(table_name=dbms_name, datas=conlist)
            print('Successful Write %s lines to %s totally writed % lines' % (cnt, dbms_name, total_cnt))
        print('All Information Completed!')

        return conlist

if __name__ == '__main__':
     print('Begin')
     cra = cralwer()
     ulist = cra.find_all_url(cra.URL,199833,cra.URL_LAST)
     write(ulist,'jjjj_ci_cqvip.txt')
     # cra.solve(dbms_name='letpub_com_cn')
     # print('Test Completed Succusseful!')
     #url = 'http://www.letpub.com.cn/index.php?page=grant&currentpage=10&name=&person=&no=&company=&startTime=2017&endTime=2017&money1=0&money2=100000000&subcategory=&addcomment_s1=0&addcomment_s2=0&addcomment_s3=0#fundlisttable'
     # for i in cra.parse_body(url):
     #     print(i)