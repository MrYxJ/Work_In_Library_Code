from analyzer.baseclass import BaseClass
from rule_ye import solution
from bs4 import BeautifulSoup
from rule_ye import GetHTMLText,GetTitleUrl,GetContent,GetWebsite,GetKeyWords,GetImg2md5,GetClassify,\
    GetDate,GetImgUrl,GetSource,GetTitle,GetUrl2md5,GetAuthor
from rule_ye import solution1
import lxml

class anhuinews(BaseClass):
    def __init__(self,url_md5 = None,content = None,url = None):
        super(BaseClass,self).__init__()
        self.url_md5 = url_md5
        self.title_url = url
        self.content = content
        self.analyse_rule = {
            'GetTitle': ['.STYLE11','.article2014_title','.article-title h1','.aticleHead h1','.biaoti'
                ,'.activeHead h2','.hot_title','font14 font','h1','head title'],
            'GetDate': ['#pubtime_baidu','.time','.article2014_tit.font9e','.pubtime_baidu','.time1 ','.time.hidden-xs',
                        '.top2','.laiyuan','.font9'],
            'GetSource': ['#source_baidu','.source','.origin','.article2014_tit.font9e','.time.hidden-xs','.laiyuan','.font9',
                          '中安在线'],
            'GetClassify': ['.dh','.position','.cell_1431_.clearfix','span[style="width:300px; height:20px; float:left; "]','span[style="width:300px; height:20px; float:left;"]',
                            '.breadcrumb','.banci'],
            'GetContent': ['#Zoom','.style50','.info','.fl.cola'],
            'GetImgUrl': ['#Zoom','.style50','.info','.article-main','.article_content.fontzw','.article2014_content_nr.alpha.fontzw','#ozoom','.pages_content','.article'],
            'GetWebsite': '中安在线',
            'GetKeyWords': None,
            #'GetAuthor':['.font9e','.author','.time.hidden-xs','.f_author','编辑']
        }


    def analyze(self):
        return solution(self.url_md5,self.title_url,self.content,self.analyse_rule)

if __name__ == '__main__':
    url = "http://finance.anhuinews.com/system/2017/12/29/007780239.shtml"
    soup = BeautifulSoup(GetHTMLText(url),'lxml')
    a = anhuinews()
    #print(GetDate(soup,a.analyse_rule['GetDate']))
    print(solution1('1', url, a.analyse_rule))
    #print(GetAuthor(soup,'ok'))
    #print(GetSource(soup,a.analyse_rule['GetSource']))
    #print(GetAuthor(soup))
    #print(GetContent(soup,a.analyse_rule['GetContent'],url))
