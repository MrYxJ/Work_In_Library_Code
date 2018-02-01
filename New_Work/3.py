#!/usr/bin/env python
#coding:utf-8
#url :http://fz.people.com.cn/skygb/sk/index.php/Index/seach
import bs4
from rule_ye import  GetHTMLText
from New_Work.new_rule_ye import Crawler
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import requests
import New_Work.Tool as Tool
from time import sleep
class cralwer(Crawler):
    URL = "http://npd.nsfc.gov.cn/"
    def clean_word(self,sstr):  # 消除一段话中所有转义符号
        return "".join(sstr.split())

    def get_check(self,url):
        try:
            response = requests.get(url)
            response.raise_for_status()
            cookiedict = requests.utils.dict_from_cookiejar(response.cookies)
            with open("check.jpg",'wb') as  f:
                f.write(response.content)
            from PIL import Image
            img = Image.open('check.jpg')
            img.show()
            code = input('老铁输入验证码（识别库老是装不上日了狗）:')
            import os
            os.remove('check.jpg')
            return code
        except Exception as e:
            print(e)

    def find_all_url(self,url = None):
        # try:
        #     headers = {
        #         'Connection': 'keep-alive',
        #         'Content-Length': '942',
        #         'Content-Type': 'application/x-www-form-urlencoded',
        #         'Host': 'npd.nsfc.gov.cn',
        #         'Cookie': 'JSESSIONID=53129E9249904D268E1450855966F83E',
        #         'Origin': 'http://npd.nsfc.gov.cn',
        #         'Referer': 'http://npd.nsfc.gov.cn/outCome_search.jsp',
        #         'Upgrade-Insecure-Requests': '1',
        #         'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.75 Safari/537.36'
        #     }
        #     data = 'currentPage=1&pageSize=6678&outcomeCategory=010&searchOutCome010.author=&searchOutCome010.title=&searchOutCome010.journalName=&searchOutCome010.year=2017&searchOutCome010.day=&searchOutCome010.page=&searchOutCome010.organization=&searchOutCome010.projectTranceNo=&searchOutCome020.author=&searchOutCome020.title=&searchOutCome020.conferenceName=&searchOutCome020.year=&searchOutCome020.month=&searchOutCome020.day=&searchOutCome020.venue=&searchOutCome020.organization=&searchOutCome020.projectTranceNo=&searchOutCome030.author=&searchOutCome030.title=&searchOutCome030.publication=&searchOutCome030.year=&searchOutCome030.ISBN=&searchOutCome030.organization=&searchOutCome030.projectTranceNo=&searchOutCome090.code=&searchOutCome090.title=&searchOutCome090.author=&searchOutCome090.organization=&searchOutCome090.category=&searchOutCome090.level=&searchOutCome090.year=&searchOutCome090.month=&searchOutCome090.day=&searchOutCome090.awardOrganization=&outcomePatent.pid=&outcomePatent.title=&outcomePatent.author=&outcomePatent.organization=&outcomePatent.patenttype=&outcomePatent.area=&outcomePatent.firstAuthorOrganization=&checkCode=%E8%AF%B7%E8%BE%93%E5%85%A5%E9%AA%8C%E8%AF%81%E7%A0%81'
        #     url = 'http://npd.nsfc.gov.cn/OutComeSearch.action'
        #     data = Tool.postman(data)
        #     response = requests.post(url, headers=headers, data=data)
        #     response.raise_for_status()
        # except requests.ConnectionError as e:
        #     print(e.args)
        #
        # soup = BeautifulSoup(response.text, 'lxml')
        # all_ul = soup.find("div", id="outcomeData").find_all('ul')
        # ulist = []
        # for ul in all_ul:
        #     hres = ul.find_all('a')
        #     ulist.append(urljoin(self.URL,hres[1]['href']))
        # Tool.write(ulist, '3.txt')
        ulist = []
        ulist = Tool.read('3.txt')
        return ulist

    def find_party(self,url):
        try:
           soup = BeautifulSoup(GetHTMLText(url),'lxml')
           peoples = soup.select('.ret_dl')
           name =''
           for p in peoples:
               name = name+self.clean_word(p.text)+' '
           return name
        except Exception:
           return None

    def find_chenguo_url(self,ulist):
        ans=""
        ok = 1
        for l in ulist:
            if ok==1 : ok=0
            else: ans = ans + ';'
            ans = ans + urljoin(self.URL,l['href'])
        return ans

    def parse_body(self,url):
        try:
            html = GetHTMLText(url)
            if html == None :return None
            soup = BeautifulSoup(html,"html.parser")
            conlist = []
            #print('tbody',tbody)
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
            ans['Pno'] = (soup.select('.jben.fir')[0].text.replace('批准号',''))
            jbens = soup.select('#right .jben')
            ans['Ptitle'] = jbens[1].text.replace('项目名称','')
            ans['Pclassify'] = jbens[2].text.replace('项目类别','')
            ans['Ano'] = jbens[3].text.replace('申请代码','')
            ans['Response'] = jbens[4].text.replace('项目负责人','')
            ans['ResponseLink'] = urljoin(self.URL,jbens[4].find('a')['href'])
            ans['Party'] = self.find_party(urljoin(self.URL,jbens[4].find('a')['href']))
            ans['Organiza'] = jbens[6].text.replace('依托单位','')
            ans['OrganizaLink'] = urljoin(self.URL,jbens[6].find('a')['href'])
            ans['Nation'] = '中国'
            ans['Term'] = jbens[7].text.replace('研究期限','')
            ans['Funds'] = jbens[8].text.replace('资助经费','')
            ans['AbstractCN'] = soup.select('.zyao .jben')[0].text
            zyao = soup.select('.zyao')[1]
            ans['KeyEN'] = zyao.select('.xmu')[0].text.replace('英文主题词','')
            ans['Summary'] = soup.select('.cguo .jben')[0].text
            ans['Url'] = url
            try:
              ans['Report'] = soup.select('div[style="padding-top:15px;"]')[0].find('a')['href']
            except:
                pass
            ans['Result'] = self.find_chenguo_url(soup.select('.cguo')[1].find_all('a'))
            #print(ans)
            #print(tuple(ans.values()))
        except Exception as e:
             print('Error url:',url)
             print(e)
        return tuple(ans.values())

    def solve(self,ulist = None,dbms_name =None):
        conlist = []
        set = {''}
        cnt = 0
        total_cnt = 0
        ulist = self.find_all_url()
        for index,url in enumerate(ulist):
            if  url in set:continue
            set.add(url)
            content = self.parse_body(url)
            if content == None : continue
            conlist.append(content)
            cnt += 1
            print('cnt:',cnt ,':url',url)
            if cnt == 500:
                total_cnt += cnt
                self.write_to_dbms(table_name=dbms_name,datas=conlist)
                print('Successful Write %s lines to %s totally writed % lines' % (cnt, dbms_name,total_cnt))
                cnt = 0
                conlist.clear()
        if len(conlist) != 0:
            total_cnt += cnt
            self.write_to_dbms(table_name=dbms_name, datas=conlist)
            print('Successful Write %s lines to %s totally writed % lines' % (cnt, dbms_name, total_cnt))
        print('All Information Completed!')
        return conlist

if __name__ == '__main__':
    cra =cralwer()
    #cra.solve()
    cra.solve(dbms_name='npd_nsfc_gov_cn')
    #cra.write_to_dbms('npd_nsfc_gov_cn')
    #url = 'http://npd.nsfc.gov.cn/projectDetail.action?pid=U1361110'
    #print(GetHTMLText(url))