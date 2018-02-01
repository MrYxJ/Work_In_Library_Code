#!/usr/bin/env python
#coding:utf-8
#Coding by MrYx(yexiaoju) in 2018.01.15

from urllib.request import urlopen
from urllib.error import HTTPError,URLError
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import  snappy,zlib,time
import requests,re,hashlib

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) ' 'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36'
}

def norm_time(time_str):
    re_str =  r'([^\d*]?)([2]?[0]?[0-1][0-9])([\s]*[.年-][\s]*)([0-1]?[0-9])([\s]*[.月-][\s]*)([0-3]?[0-9])([^\d]+)?([0-2]?[0-9]\:)?([0-5][0-9])?(\:[0-5][0-9])?'
    Time = re.search(re_str,time_str)
    #print('Time:',Time.group(4))
    if Time :
        year = month = day = hour = minute = second =''
        year = Time.group(2)
        if year == None:
            year = '2017';month = Time.group(2);day = Time.group(4);hour = Time.group(6); seond = Time.group(9)
        elif len(year) == 2: year = '20'+year
        month = Time.group(4) ; day = Time.group(6)
        if Time.group(9) :
            hour = Time.group(8); minute  = Time.group(9)
        if Time.group(10) :
           second = Time.group(10)
        return(year+'-'+month+'-'+day+' '+hour+minute+second)#神奇系统自动补全hour mimute second之间的:
    else:
        return None

def clean_word(sstr):#消除一段话中所有转义符号
    # 三个特殊字符\xc2、\xa0、\u3000
    escape_set = {'&ensp;': ' ', '&#8194;':' ', '&emsp;': ' ', '&#8195;': ' ', '&nbsp;': ' ', '&#160;': ' ',
                  '&#32;': ' ',
                  '&lt;': '<', '&#60;': '<', '&gt;': '>', '&#62;': '>', '&amp;': '&', '&#38;': '&', '&quot;': '"',
                  '&#34;': '"',
                  '&copy;': '©', '&#169;': '©', '&reg;': '®', '&#174;': '®', '&trade;': '™', '&#8482;': '™',
                  '&times;': '×',
                  '&#215;': '×', '&divide;': '÷', '&#247;': '÷', 'Â': ' ', '　':' '}
    for key, value in escape_set.items():
        sstr = sstr.replace(key, value)
    return "".join(sstr.split())

def clean_word_scriptstyle(soup):#消除一段html形式文本里面<script>标签内js代码
    words = str(soup)
    sub_script = re.compile(r'<script[^>]*?>[\s|\S]*?</script>')
    words = sub_script.sub('',words)
    sub_style = re.compile(r'<style[^>]*?>[\s|\S]*?</style>')
    words = sub_style.sub('', words)
    soup = BeautifulSoup(words, 'lxml')
    return soup

def GetHTMLText(url):
    try:
        r = requests.get(url,headers = headers)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except Exception as e:
        print('url:',url)
        return None

def GetTitle(soup,pos): #通过pos定位 到标题
    try:
        for p in pos:
            test = soup.select(p)
            if test == [] :continue
            test = test[0].text.strip()
            if test: return clean_word(test)
    except:
        return None

def GetDate(soup,pos): #兼顾以前并且优化成对全文过滤掉标签后正则匹配，不需要找参数
    try:
        for p in pos:
            test = soup.select(p)
            #print('test',test)
            if test == [] :continue
            test = test[0].text.strip()
            #print('test===',test)
            if test: return norm_time(test)
        else :
            #print('pre',soup.prettify())
            soup = clean_word_scriptstyle(soup)
            #print("---------------------")
            #print('last',soup.prettify())
            test = clean_word(soup.text)
            #print('test',test)
            if norm_time(test):
                return norm_time(test)
    except Exception as e:
        print('Error Information:',e)
        return None

def GetSource(soup,pos):#兼顾以前的写法，实现从一段文字中找到来源:取分号后面内容，如果没有来源还是得定位啊
    try:
        for p in pos:
            test = soup.select(p)
            if test == []: continue
            test = test[0].text.strip()
            word = re.compile(r'([^\u4e00-\u9fa5]*)?([\u4e00-\u9fa5]*)([^\u4e00-\u9fa5]*)')
            math = word.search(test)
            return clean_word(math.group(2))
    except:      #新的思路，直接去过滤后全文后面找来源后面的汉字
        soup = clean_word_scriptstyle(soup)
        test = soup.text
        index = test.find("来源")
        word = re.compile(r'([^\u4e00-\u9fa5]*)?([\u4e00-\u9fa5]*)')
        math = word.search(test[index + 3:])
        if math.group(2) != None:
            return clean_word(math.group(2))
        else:
            return pos[-1]

def GetClassify(soup,pos):
    try:
        for p in pos:
            test = soup.select(p)
            if test == [] : continue
            test = test[len(soup.select(p))-1]
            #print('type(test)',type(test))
            Words = clean_word_scriptstyle(test)
            Words = Words.text
            if Words:
                return clean_word(Words)
    except:
        return None

def GetUrl2md5(url):
    m = hashlib.md5()
    m.update(url.encode('utf-8'))
    return m.hexdigest()

def GetImgUrl(url,soup,pos):#只找正文下面的图片
    try:
        #print('pos==',pos)
        for p in pos:
            Words = soup.select(p)
            #print('???????',Words)
            if Words == []: continue
            Words = Words[0]
            #print('!!!!!',Words)
            images = Words.find_all("img")
            #print("images",images)
            List = []
            for image in images:
                List.append((urljoin(url, image['src'])))
            #print('List==',List)
            if List != []:
                #print('pos:',p)
                return '；'.join(List)
    except:
        return None

def GetImg2md5(url,soup,pos):
    try:
        List = GetImgUrl(url,soup,pos)
        List = List.split('；')
        #print('List',List)
        List2 =[]
        for url in List:
             List2.append(GetUrl2md5(url))
        if List2: return '；'.join(List2)
    except:
        return None

def GetTitleUrl(url):
    if '#' in url:
        url = url[:url.find('#')]
    return url

def GetContent(soup,pos,url):
    try:
        for p in pos:
            #print('soup',soup.prettify())
            Words = soup.select(p)
            #print('Words',Words)
            if Words == [] :continue
            Words = Words[0] # 解析出一段html文本
            Images = Words.find_all("img")
            images = []
            for image in Images:
                images.append(GetUrl2md5(urljoin(url,image['src'])))
            words = str(Words)
            for image in images:
                img = re.compile(r'<img[^s]*?src=[^>]*?>([^<]*</img>)?')
                words = img.sub('(img src='+image+'/)',words,count=1) #count=1只替换每次匹配的第一个，没有count默认匹配所有
            sub_script = re.compile(r'<script[^>]*?>[\s\S]*?</script>')
            words = sub_script.sub('', words)
            sub_style = re.compile(r'<style[^>]*?>[\s|\S]*?</style>')
            words = sub_style.sub('', words)
            Words = BeautifulSoup(words, 'lxml')
            Words = Words.text
            words = str(Words)
            words = words.replace("(","<")
            words = words.replace(")",">")
            if words :
                return clean_word(words).replace('imgsrc','img src')
    except:
        return None

def GetWebsite(soup,name):
    return name

def GetKeyWords(soup):
    try:
        keyword = soup.find_all("meta",{"name":{"keywords","Keywords","KEYWORDS"}})[0]['content']
        if keyword:
            Re = re.compile('[\s]+|[\,]')
            keyword = Re.sub(';', keyword)
            return keyword
    except:
        pass
    return None

def DecodeHtml(html):
    List = ["utf-8","gbk","gb18030","gb2312"]
    for i in List:
        try:
            html2 = html.decode(i)
            if html2 : return html2
        except:
            continue
    return None

def GetAuthorFromHead(soup):
    try:
        keyword = soup.find_all("meta", {"name": {"author"}})[0]['content']
        #print('keyword:',keyword)
        if keyword:
            Re = re.compile('[\s]+|[\,]')
            keyword = Re.sub(';', keyword)
            return keyword
    except: return None
    else : return None

def GetAuthor(soup): #先把全文里script和其他各种标签去掉，再用正则找文字里编辑，作者等后面内容，所以这个也不需要传入参数
    try:
        soup = clean_word_scriptstyle(soup)
        test = soup.text
        name = re.search(r'([^\u4e00-\u9fa5]*)?(编辑)([^\u4e00-\u9fa5]*)?([\u4e00-\u9fa5-a-z0-9A-Z]+)?',test)
        if name == None: name = re.search(r'([^\u4e00-\u9fa5]*)?(作者)([^\u4e00-\u9fa5]*)?([\u4e00-\u9fa5-a-z0-9A-Z]+)?',test)
        if name == None: name = re.search(r'([^\u4e00-\u9fa5]*)?(记者)([^\u4e00-\u9fa5]*)?([\u4e00-\u9fa5-a-z0-9A-Z]+)?',test)
        if name == None: name = re.search(r'([^\u4e00-\u9fa5]*)?(责编)([^\u4e00-\u9fa5]*)?([\u4e00-\u9fa5-a-z0-9A-Z]+)?', test)
        if name == None:return '编辑'
        elif name.group(2) !=None and name.group(4) == None: return '编辑'
        else:
            return name.group(4)
    except:
        if GetAuthorFromHead(soup):
            return GetAuthorFromHead(soup)
        return '编辑'
    else:
        if GetAuthorFromHead(soup):
            return GetAuthorFromHead(soup)
        return '编辑'
# def GetAuthor(soup,pos):
#     try:
#         #print('ok')
#         for p in pos:
#             test = soup.select(p)
#             if test == []: continue
#             test = test[0].text.strip()
#             #print('test:',test)
#             author = re.compile(r'([^\u4e00-\u9fa5]*)?(编辑|作者|记者|通讯员)([^\u4e00-\u9fa5]*)?([\u4e00-\u9fa5-a-z0-9A-Z]+)?')
#             name = re.search(author,test)
#             if name == None:return test
#             elif name.group(2) !=None and name.group(4) == None: return pos[-1]
#             else: return name.group(4)
#     except:
#         if GetAuthorFromHead(soup):
#             return GetAuthorFromHead(soup)
#         return pos[-1]
#     else:
#         if GetAuthorFromHead(soup):
#             return GetAuthorFromHead(soup)
#         return pos[-1]
def compress(content):
    if content:
        content = snappy.compress(content)
    return content

def solution(url_md5, title_url,content, ana_rule):
    html = zlib.decompress(content)
    #html = snappy.decompress(content)
    decode_html = DecodeHtml(html)
    if decode_html:
        soup = BeautifulSoup(decode_html, 'lxml')
    else :
        return None

    answer = {  'url_md5':'',  #文章详情页链接MD5加密(唯一索引)
                'title':'',  #文章标题-->中国不让过圣诞节？环球时报:事实是大
                'date':'',  #文章发布时间-->2017年12月25日 08:14
                'source':'',  #文章来源网站-->环球网
                'classify':'',  #文章分类--> 新闻中心>国内新闻>正文
                'content':'',  #正文
                'img_urls': '',  # 图片绝对地址链接（多项用；隔开）
                'img_md5': '',  # 图片绝对地址链接MD5加密（多项用；隔开）
                'title_url':'',  #文章详情页绝对地址链接（#号后面的全部去掉）
                'keywords':'',  #文章关键字-->圣诞节（用；隔开）
                'website':'',  #所采集的网站-->新浪网
                'add_time':'',  #数据插入时间，获取服务器当前时间即可
                'author':''
            }
    add_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    #print("title",GetTitle(soup,ana_rule['GetTitle']))
    if GetContent(soup,ana_rule['GetContent'],title_url) == None or GetTitle(soup,ana_rule['GetTitle']) == None:return None
    answer = (url_md5,GetTitle(soup,ana_rule['GetTitle']),GetDate(soup,ana_rule['GetDate']),GetSource(soup,ana_rule['GetSource']),GetClassify(soup,ana_rule['GetClassify']),
             compress(GetContent(soup,ana_rule['GetContent'],title_url)),GetImgUrl(title_url,soup,ana_rule['GetImgUrl']),GetImg2md5(title_url,soup,ana_rule['GetImgUrl']),title_url,GetKeyWords(soup),
             GetWebsite(soup,ana_rule['GetWebsite']),add_time,GetAuthor(soup))
    return answer

def solution1(url_md5, title_url,ana_rule):
    #print('url',title_url,'   ana_rule',ana_rule)
    try:
        soup = BeautifulSoup(GetHTMLText(title_url), 'lxml')
        answer = {'url_md5':'',#文章详情页链接MD5加密(唯一索引)
                   'title':'',#文章标题-->中国不让过圣诞节？环球时报:事实是大
                    'date':'',#文章发布时间-->2017年12月25日 08:14
                    'source':''
                             ''
                             'meiyouwenti',#文章来源网站-->环球网
                    'classify':'',#文章分类--> 新闻中心>国内新闻>正文
                    'content':'',#正文
                    'img_urls':'',#图片绝对地址链接（多项用；隔开）
                    'img_md5':'',#图片绝对地址链接MD5加密（多项用；隔开）
                    'title_url':'',#文章详情页绝对地址链接（#号后面的全部去掉）
                    'keywords':'',#文章关键字-->圣诞节（用；隔开）
                    'website':'',#所采集的网站-->新浪网
                    'add_time':'',#数据插入时间，获取服务器当前时间即可
                    'author': ''
        }
        add_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        return (url_md5,GetTitle(soup,ana_rule['GetTitle']),GetDate(soup,ana_rule['GetDate'])
                ,GetSource(soup,ana_rule['GetSource']),GetClassify(soup,ana_rule['GetClassify']),
                GetContent(soup,ana_rule['GetContent'],title_url),GetImgUrl(title_url,soup,ana_rule['GetImgUrl']),
                GetImg2md5(title_url,soup,ana_rule['GetImgUrl']),title_url,GetKeyWords(soup),
                GetWebsite(soup,ana_rule['GetWebsite']),add_time,GetAuthor(soup)
                )
    except Exception as e:
        return None

if __name__ == '__main__':
    # ssss = "\r\n 体育新闻\r\n"
    # print(clean_word(ssss))
    re_str = r'([^\d*]?)([\d][\d][\d][\d])([^d]*?)(\d{1,2})([^\d]*?)(\d{1,2})([^\d]*)?(\d{1,2}\:)?(\d{1,2})?(\:\d{1,2})?'
    da ='11-12-05 10:21:21','11-22 09:12:34','11-22 09:07','重庆文明网2016年  08月15日10:57:36',\
        '17年12月10号 18:27:19','日期:[2012年10月22日] 你好','2018-01-16 14:45','2018-01-15 20:11:31',\
        '2016-10-10 07:18','2018年10月06日 7:20'
    for i in da:
        print(norm_time(i))
    keyword ='a  b  c'
    Re = re.compile('[\s]+|[\,]')
    keyword = Re.sub(';', keyword)
    print('keyword',keyword)
    print("Thank's for using this coded by MrYx(Yexiaoju) in 2018.01.15!")
    #([^\d*]?)([\d]{2,4})([^d]*?)(\d{1,2})([^\d]*?)(\d{1,2})([^\d]*)?(\d{1,2}\:)?(\d{1,2})?(\:\d{1,2})? old
    #([^\d*]?)([2]?[0]?[0-1][0-9])?([\s]*[.年-][\s]*)?([0-1]?[0-9])([\s]*[月.-][\s]*)([0-3]?[0-9])([^\d]+)?([0-2]?[0-9]\:)?([0-5][0-9])?(\:[0-5][0-9])?