from analyzer.baseclass import BaseClass
from rule_ye import solution
from bs4 import BeautifulSoup
from rule_ye import GetHTMLText,GetTitleUrl,GetContent,GetWebsite,GetKeyWords,GetImg2md5,GetClassify,GetDate,GetImgUrl,GetSource,GetTitle,GetUrl2md5
from rule_ye import solution1

class xinjiangnet(BaseClass):
    def __init__(self,url_md5 = None,content = None,url = None):
        super(BaseClass,self).__init__()
        self.url_md5 = url_md5
        self.title_url = url
        self.content = content
        self.analyse_rule = {
            'GetTitle': ['h1.article-title','.h1','strong','.article-title'],
            'GetDate': ['.date','.post-time','td[style="font-size:12px;"]'],
            'GetSource': ['.source'],
            'GetClassify': ['div[style="margin-top:8px; float:right; display:block;; float:right; display:block;"]','.crumb','#123'],
            'GetContent': ['.article-content.fontSizeSmall.BSHARE_POP','p[class="summary"]','.gallery-photo-description','.TRS_Editor'],
            'GetImgUrl':  ['.article-content.fontSizeSmall.BSHARE_POP','p[class="summary"]','.gallery-photo-description','.TRS_Editor'],
            'GetWebsite': '新疆网',
            'GetKeyWords': None,
            'GetAuthor': ['author','.editors','.editor','编辑']
        }

    def analyze(self):
        return solution(self.url_md5,self.title_url,self.content,self.analyse_rule)

if __name__ == '__main__':
    url = "http://www.xinjiangnet.com.cn/2016/1118/1689637.shtml"
    soup = BeautifulSoup(GetHTMLText(url), 'html.parser')
    a = xinjiangnet()
    #print(GetClassify(soup,a.analyse_rule['GetClassify']))
    #print(GetTitle(soup,a.analyse_rule['GetTitle']))
    #print(GetDate(soup,a.analyse_rule['GetDa
    print(solution1('1',url,a.analyse_rule))
    #print(GetImgUrl(url,soup,a.analyse_rule["GetImgUrl"]))
    #print(GetSource(soup,a.analyse_rule['GetSource']))
    #print(GetContent(soup,a.analyse_rul e["GetContent"],url))
    #print(GetImg2md5(url,soup,a.analyse_rule["GetImgUrl"]))