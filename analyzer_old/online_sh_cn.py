from analyzer.baseclass import BaseClass
from rule_ye import solution
from bs4 import BeautifulSoup
from rule_ye import GetHTMLText,GetTitleUrl,GetContent,GetWebsite,GetKeyWords,GetImg2md5,\
    GetClassify,GetDate,GetImgUrl,GetSource,GetTitle,GetUrl2md5,GetAuthor
from rule_ye import solution1

class online_sh(BaseClass):
    def __init__(self,url_md5 = None,content = None,url = None):
        super(BaseClass,self).__init__()
        self.url_md5 = url_md5
        self.title_url = url
        self.content = content
        self.analyse_rule = {
            'GetTitle': ['h1','#headline'],
            'GetDate': ['#source'],
            'GetSource': ['#source'],
            'GetClassify': ['.crump'],
            'GetContent': ['.newsCon'],
            'GetImgUrl':  ['.newsCon'],
            'GetWebsite': '上海热线',
            'GetKeyWords': None,
            'GetAuthor': ['editors','editor','编辑']
        }

    def analyze(self):
        return solution(self.url_md5,self.title_url,self.content,self.analyse_rule)

if __name__ == '__main__':
    url = "http://hot.online.sh.cn/content/2018-01/23/content_8755802.htm"
    soup = BeautifulSoup(GetHTMLText(url), 'html.parser')
    a = online_sh()
    #print(GetClassify(soup,a.analyse_rule['GetClassify']))
    #print(GetTitle(soup,a.analyse_rule['GetTitle']))
    #print(GetDate(soup,a.analyse_rule['GetDa
    print(solution1('1',url,a.analyse_rule))
    #print(GetSource(soup,a.analyse_rule['GetSource']))