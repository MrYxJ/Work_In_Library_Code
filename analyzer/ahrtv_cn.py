from analyzer.baseclass import BaseClass
from rule_ye import solution
from bs4 import BeautifulSoup
from rule_ye import GetHTMLText,GetTitleUrl,GetContent,GetWebsite,GetKeyWords,GetImg2md5,GetClassify,\
    GetDate,GetImgUrl,GetSource,GetTitle,GetUrl2md5,GetAuthor
from rule_ye import solution1

class ahrtv(BaseClass):
    def __init__(self,url_md5 = None,content = None,url = None):
        super(BaseClass,self).__init__()
        self.url_md5 = url_md5
        self.title_url = url
        self.content = content
        self.analyse_rule = {
            'GetTitle': ['.article2014_title','.article-title h1','.aticleHead h1','.biaoti'
                ,'.activeHead h2','.hot_title','font14 font','head title'],
            'GetDate': ['.article2014_tit.font9e','.pubtime_baidu','.time1 ','.time.hidden-xs',
                        '.top2','.laiyuan','.font9'],
            'GetSource': ['.origin','.article2014_tit.font9e','.time.hidden-xs','.laiyuan','.font9','科技日报'],
            'GetClassify': ['.cell_1431_.clearfix','span[style="width:300px; height:20px; float:left; "]','span[style="width:300px; height:20px; float:left;"]','.breadcrumb','.banci'],
            'GetContent': ['#playerDrag','.w1000','.article-main','.article_content.fontzw','.article2014_content_nr.alpha.fontzw','.font10','.content','#ozoom','.pages_content','.article','.font10.tl.alpha'],
            'GetImgUrl': ['.article-main','.article_content.fontzw','.article2014_content_nr.alpha.fontzw','.content','#ozoom','.pages_content','.article'],
            'GetWebsite': '安徽网络广播电视台',
            'GetKeyWords': None,
            #'GetAuthor':['.font9e','.author','.time.hidden-xs','.f_author','编辑']
        }

    def analyze(self):
        return solution(self.url_md5,self.title_url,self.content,self.analyse_rule)

if __name__ == '__main__':
    url = "http://www.ahrtv.cn/news/system/2018/01/22/004279636.shtml"
    soup = BeautifulSoup(GetHTMLText(url), 'html.parser')
    a = ahrtv()
    # print(GetDate(soup,a.analyse_rule['GetDate']))
    print(solution1('1', url, a.analyse_rule))
    #print(GetAuthor(soup,'ok'))
    #print(GetSource(soup,a.analyse_rule['GetSource']))
    #print(GetAuthor(soup,a.analyse_rule['GetAuthor']))
