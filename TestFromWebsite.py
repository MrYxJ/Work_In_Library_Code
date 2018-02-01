#usr/env python
#coding:utf-8
#coded by MrYx 2018.01.25

import re
import requests
from queue import Queue
from bs4 import BeautifulSoup
from rule_ye import GetHTMLText
from rule_ye import solution1
from analyzer.ahrtv_cn import ahrtv


def getlinks(url):
    try:
        html = GetHTMLText(url)
        soup = BeautifulSoup(html, 'html.parser')
        return soup.find_all('a')
    except:
        return None

def check(url, name, Set):
    key = re.compile(name)
    if key.search(url) != None and url not in Set and "bbs" not in url and \
        (url.startswith('www') or url.startswith('http')) and 'folder' not in url:
        return True
    else :
        return False

def bfs_links(url,name):
    answer = [];
    que = Queue()
    Set ={url};
    try:
      for link  in getlinks(url):
        try:
            url_n = link['href']
            if check(url_n, name,Set):
                que.put(url_n)
                Set.add(url_n)
                answer.append(url_n)
        except: pass
    except:pass

    total_num = 15; cnt=0
    while cnt<total_num and que.empty() is False:
        cnt = cnt+1
        url_n = que.get()
        try:
          for link in getlinks(url_n):
            try:
             url_nxt = link['href']
             if check(url_nxt, name, Set):
                que.put(url_nxt)
                Set.add(url_nxt)
                answer.append(url_nxt)
            except: pass
        except:pass
    return answer

file_name = 'ahrtv'

def write(links):
    with open(file_name+'.txt','w') as f:
        for l in links:
            f.writelines(l+'\n')

def read():
    links = []
    with open(file_name+'.txt','r') as f:
        while True:
            sstr = f.readline()
            if not sstr: break
            links.append(sstr)
    return links

def check_empty(ans):
    list =[1,2,3,4,12]
    for i in list:
        if ans[i]== None :return True
    return False

def test(links):
    a = ahrtv()
    total = 0 ;true_cnt = 0
    ErrorLink = []
    for url in links:
        total += 1
        ans = solution1('1',url.strip(),a.analyse_rule)
        if ans == None: continue
        try:
            if ans[1] !=None and ans[5] !=None:
                print("{0:{5}^35}\t{1:{5}^15}\t{2:{5}^8}\t{3:{5}^15}\t{4:{5}^6}".format(ans[1],ans[2],ans[3],ans[4],ans[12],chr(12288)))
                if(check_empty(ans)) : print('{0:{2}^20}\t{1:^20}'.format(ans[1],url.strip(),chr(12288)))
                true_cnt += 1
            else:
                ErrorLink.append(url)
                print('Error : ',url)
        except Exception as e:
            ErrorLink.append(url)
            print('Except url:',url)
    write(ErrorLink)

    #print("测试[%s]条解析成功的比例为[%.2f]"%(true_cnt/total))

if __name__ == '__main__':
    #url = 'http://news.anhuinews.com/'
    #print(check('ahrtv/bbs/.com','ahrtv'))
    #test_links = bfs_links(url,'anhuinews')
    #write(test_links)
    test_links = read()
    print('一共爬取:%s个网站'% len(test_links))
    test(test_links)



