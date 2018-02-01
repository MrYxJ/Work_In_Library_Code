from analyzer.baseclass import BaseClass
from rule_ye import solution
from bs4 import BeautifulSoup
from rule_ye import GetHTMLText,GetTitleUrl,GetContent,GetWebsite,GetKeyWords,GetImg2md5,\
    GetClassify,GetDate,GetImgUrl,GetSource,GetTitle,GetUrl2md5,GetAuthor
from rule_ye import solution1

class sxdaily(BaseClass):
    def __init__(self,url_md5 = None,content = None,url = None):
        super(BaseClass,self).__init__()
        self.url_md5 = url_md5
        self.title_url = url
        self.content = content
        self.analyse_rule = {
            'GetTitle': ['.container.title h1','#p_title','.text.width1000.clearfix h1',
                         '.p_title','.bmnr_con_biaoti','.content h3'],
            'GetDate': ['.container.title div p','.text.width1000.clearfix h3','.tools',
                        '.content.fl p','span'],
            'GetSource': ['.container.title div p a','.tools','.text.width1000.clearfix h3',
                          '陕西传媒网'],
            'GetClassify': ['.local_nav'],
            'GetContent': ['#zoom','.text.width1000.clearfix','.content'],
            'GetImgUrl':  ['#zoom','.text.width1000.clearfix','.content'],
            'GetWebsite': '陕西传媒网',
            'GetKeyWords': None,
            'GetAuthor': ['editors','author','editor','h3[style="font-size:12px;"]','.container.title p','.editor','编辑']
        }

    def analyze(self):
        return solution(self.url_md5,self.title_url,self.content,self.analyse_rule)

if __name__ == '__main__':
    url = "http://www.sxdaily.com.cn/n/2018/0122/c508-6314082.html"
    soup = BeautifulSoup(GetHTMLText(url), 'html.parser')
    a = sxdaily()
    #print(GetClassify(soup,a.analyse_rule['GetClassify']))
    #print(GetTitle(soup,a.analyse_rule['GetTitle']))
    #print(GetDate(soup,a.analyse_rule['GetDa
    print(solution1('1',url,a.analyse_rule))
    #print(GetSource(soup,a.analyse_rule['GetSource']))