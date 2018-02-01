from analyzer.baseclass import BaseClass
from rule_ye import solution
from bs4 import BeautifulSoup
from rule_ye import GetHTMLText,GetTitleUrl,GetContent,GetWebsite,GetKeyWords,GetImg2md5,GetClassify,GetDate,GetImgUrl,GetSource,GetTitle,GetUrl2md5
from rule_ye import solution1

class xian(BaseClass):
    def __init__(self,url_md5 = None,content = None,url = None):
        super(BaseClass,self).__init__()
        self.url_md5 = url_md5
        self.title_url = url
        self.content = content
        self.analyse_rule = {
            'GetTitle': ['.container','.biaoti','td.bt1','p.title_main','.cont_maint','.ina_news_text h1 p b','#pictitle_main','.title'],
            'GetDate': ['.shux_12','.article-infos span', '.mess', '.main', 'span.ina_data','#pic_xinxi'],
            'GetSource': ['.shux_12','.mess a', 'span.news_icon','.pic_xinxi','西安晚报'],
            'GetClassify': ['#position', '.bt3', '.ina_place p'],
            'GetContent': ['p[align="center"]','div[id="context"]','.content', '#content', 'td[valign="top"]', '.ina_content '],
            'GetImgUrl':  ['p[align="center"]','div[id="context"]','.content', '#content', 'td[valign="top"]', '.ina_content '],
            'GetWebsite': '西安新闻网',
            'GetKeyWords': None,
            'GetAuthor': ['author','.mess','editors','editor', '编辑']
        }

    def analyze(self):
        return solution(self.url_md5,self.title_url,self.content,self.analyse_rule)

if __name__ == '__main__':
    url = "http://www.xiancn.com/gb/wbpaper/2007-12/21/content_1410877.htm"
    soup = BeautifulSoup(GetHTMLText(url), 'html.parser')
    a = xian()
    #print(GetClassify(soup,a.analyse_rule['GetClassify']))
    #print(GetTitle(soup,a.analyse_rule['GetTitle']))
    #print(GetDate(soup,a.analyse_rule['GetDate'
    print(solution1('1',url,a.analyse_rule))
    #print(GetSource(soup,a.analyse_rule['GetSource']))