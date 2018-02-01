from analyzer.baseclass import BaseClass
from rule_ye import solution
from bs4 import BeautifulSoup
from rule_ye import GetHTMLText,GetTitleUrl,GetContent,GetWebsite,GetKeyWords,GetImg2md5,\
    GetClassify,GetDate,GetImgUrl,GetSource,GetTitle,GetUrl2md5,GetAuthor
from rule_ye import solution1

class nxnet(BaseClass):
    def __init__(self,url_md5 = None,content = None,url = None):
        super(BaseClass,self).__init__()
        self.url_md5 = url_md5
        self.title_url = url
        self.content = content
        self.analyse_rule = {
            'GetTitle': ['.con_title','h1.article-title'],
            'GetDate': ['.time','.date'],
            'GetSource': ['.cite','.source'],
            'GetClassify': ['.cur_location'],
            'GetContent': ['article'],
            'GetImgUrl':  ['article'],
            'GetWebsite': '宁夏网',
            'GetKeyWords': None,
            'GetAuthor': ['editors','editor','div[style="padding:20px 0;  font-size:14px;"]', '编辑']
        }

    def analyze(self):
        return solution(self.url_md5,self.title_url,self.content,self.analyse_rule)

if __name__ == '__main__':
    url = "http://nxnet.cn/hd/201801/t20180112_2361922.html"
    soup = BeautifulSoup(GetHTMLText(url), 'html.parser')
    a = nxnet()
    #print(GetClassify(soup,a.analyse_rule['GetClassify']))
    #print(GetTitle(soup,a.analyse_rule['GetTitle']))
    #print(GetDate(soup,a.analyse_rule['GetDa
    print(solution1('1',url,a.analyse_rule))
    print(GetAuthor(soup, a.analyse_rule["GetAuthor"]))
    #print(GetSource(soup,a.analyse_rule['GetSource']))