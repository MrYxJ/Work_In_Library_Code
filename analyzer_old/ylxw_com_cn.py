from analyzer.baseclass import BaseClass
from rule_ye import solution
from bs4 import BeautifulSoup
from rule_ye import GetHTMLText,GetTitleUrl,GetContent,GetWebsite,GetKeyWords,GetImg2md5,GetClassify,GetDate,GetImgUrl,GetSource,GetTitle,GetUrl2md5
from rule_ye import solution1


class ylxw(BaseClass):
    def __init__(self,url_md5 = None,content = None,url = None):
        super(BaseClass,self).__init__()
        self.url_md5 = url_md5
        self.title_url = url
        self.content = content
        self.analyse_rule = {
            'GetTitle': ['.article-content-title', '.title h1','#title1'],
            'GetDate': ['.date.fl-l', '.article-infos span','#publishdate'],
            'GetSource': ['.source.fl-l', 'p.from.f-l','新疆日报'],
            'GetClassify': ['.curNews.domPC', 'p.position '],
            'GetContent': ['.article-detail-inner.article-relevance.w660.ov', '.cont-wrap p','#content'],
            'GetImgUrl': ['.article-detail-inner.article-relevance.w660.ov', '.cont-wrap p','#content'],
            'GetWebsite': '伊犁新闻网',
            'GetKeyWords': None,
            'GetAuthor':['author','.mess','editor','editors','编辑']
        }

    def analyze(self):
        return solution(self.url_md5,self.title_url,self.content,self.analyse_rule)

if __name__ == '__main__':
    url = "http://fms.news.cn/swf/2018qmtt/1_23_2018_zf/index.html"
    soup = BeautifulSoup(GetHTMLText(url), 'html.parser')
    a = ylxw()
    # print(GetDate(soup,a.analyse_rule['GetDate']))
    print(solution1('1', url, a.analyse_rule))
