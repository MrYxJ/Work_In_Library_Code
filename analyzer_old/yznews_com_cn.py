from analyzer.baseclass import BaseClass
from rule_ye import solution
from bs4 import BeautifulSoup
from rule_ye import GetHTMLText,GetTitleUrl,GetContent,GetWebsite,GetKeyWords,GetImg2md5,GetClassify,GetDate,GetImgUrl,GetSource,GetTitle,GetUrl2md5,GetAuthor
from rule_ye import solution1


class yznews(BaseClass):
    def __init__(self,url_md5 = None,content = None,url = None):
        super(BaseClass,self).__init__()
        self.url_md5 = url_md5
        self.title_url = url
        self.content = content
        self.analyse_rule = {
            'GetTitle': ['.hd h1','head title'],
            'GetDate': ['.pubTime','.ta'],
            'GetSource': ['.info a'],
            'GetClassify': ['div[style="float:left;height:30px;margin-left:18px;"]','table[align="center" width="100%"]'],
            'GetContent': ['#Cnt-Main-Article-QQ'],
            'GetImgUrl':  ['.bd','.#Cnt-Main-Article-QQ','table[align="center"]'],
            'GetWebsite': '扬州网',
            'GetKeyWords': None,
            'GetAuthor' : ['author','editors','editor','#Cnt-Main-Article-QQ','编辑']
        }

    def analyze(self):
        return solution(self.url_md5,self.title_url,self.content,self.analyse_rule)

if __name__ == '__main__':
    url = "http://exporter.yznews.com.cn/?id=1380"
    soup = BeautifulSoup(GetHTMLText(url), 'html.parser')
    a = yznews()
    print(solution1('1', url, a.analyse_rule))
    #print(GetClassify(soup,a.analyse_rule['GetClassify']))
    #print(GetTitle(soup,a.analyse_rule['GetTitle']))
    #print(GetDate(soup,a.analyse_rule['GetDa
    #print(solution1('1',url,a.analyse_rule))
    #print(GetImgUrl(url,soup,a.analyse_rule["GetImgUrl"]))
    #print(GetSource(soup,a.analyse_rule['GetSource']))
    #print(GetContent(soup,a.analyse_rule["GetContent"],url))
    #print(GetImg2md5(url,soup,a.analyse_rule["GetImgUrl"]))