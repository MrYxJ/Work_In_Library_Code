from analyzer.baseclass import BaseClass
from rule_ye import solution
from bs4 import BeautifulSoup
from rule_ye import GetHTMLText,GetTitleUrl,GetContent,GetWebsite,GetKeyWords,GetImg2md5,GetClassify,GetDate,GetImgUrl,GetSource,GetTitle,GetUrl2md5
from rule_ye import solution1


class chinaqw(BaseClass):
    def __init__(self,url_md5 = None,content = None,url = None):
        super(BaseClass,self).__init__()
        self.url_md5 = url_md5
        self.title_url = url
        self.content = content
        self.analyse_rule = {
            'GetTitle': ['.blueb','.content h1', 'span.105w', 'p[align="center"]','.banner_pic','head title'],
            'GetDate': ['.left-t', 'div[align="center"]','.info'],
            'GetSource': ['.left-t a', "中国侨网"],
            'GetClassify': ['.qw_listmbx', 'td[width="261"]','a[href="/index.shtml"]'],
            'GetContent': ['.content', '.old', 'div[align="left"]','#alldiv','p'],
            'GetImgUrl': ['.content','.old','#alldiv'],
            'GetWebsite': '中国侨网',
            'GetKeyWords': None,
            'GetAuthor':['.editor','.editors','编辑']
        }

    def analyze(self):
        return solution(self.url_md5,self.title_url,self.content,self.analyse_rule)

if __name__ == '__main__':
    url = "http://www.chinaqw.com/hqhr/hrdt/200908/30/178029.shtml"
    soup = BeautifulSoup(GetHTMLText(url), 'html.parser')
    a = chinaqw()
    #print(GetClassify(soup,a.analyse_rule['GetClassify']))
    #print(GetTitle(soup,a.analyse_rule['GetTitle']))
    #print(GetDate(soup,a.analyse_rule['GetDate']))
    print(solution1('1',url,a.analyse_rule))
    #print(GetSource(soup,a.analyse_rule['GetSource']))