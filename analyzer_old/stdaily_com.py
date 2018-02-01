from analyzer.baseclass import BaseClass
from rule_ye import solution
from bs4 import BeautifulSoup
from rule_ye import GetHTMLText,GetTitleUrl,GetContent,GetWebsite,GetKeyWords,GetImg2md5,GetClassify,\
    GetDate,GetImgUrl,GetSource,GetTitle,GetUrl2md5,GetAuthor
from rule_ye import solution1

class stdaily(BaseClass):
    def __init__(self,url_md5 = None,content = None,url = None):
        super(BaseClass,self).__init__()
        self.url_md5 = url_md5
        self.title_url = url
        self.content = content
        self.analyse_rule = {
            'GetTitle': ['.aticleHead h1','.biaoti','.activeHead h2','.hot_title'],
            'GetDate': ['.time1 ','.time.hidden-xs','.top2','.laiyuan'],
            'GetSource': ['.time.hidden-xs','.laiyuan','科技日报'],
            'GetClassify': ['.breadcrumb','.banci'],
            'GetContent': ['.content','#ozoom','.pages_content','.article'],
            'GetImgUrl': ['.content','#ozoom','.pages_content','.article'],
            'GetWebsite': '中国科技网',
            'GetKeyWords': None,
            'GetAuthor':['.author','.time.hidden-xs','.f_author','编辑']
        }

    def analyze(self):
        return solution(self.url_md5,self.title_url,self.content,self.analyse_rule)

if __name__ == '__main__':
    url = "http://stdaily.com/index/toutiao/2017-07/11/content_559247.shtml"
    soup = BeautifulSoup(GetHTMLText(url), 'html.parser')
    a = stdaily()
    # print(GetDate(soup,a.analyse_rule['GetDate']))
    print(solution1('1', url, a.analyse_rule))
    #print(GetSource(soup,a.analyse_rule['GetSource']))
    #print(GetAuthor(soup,a.analyse_rule['GetAuthor']))
