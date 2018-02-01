from analyzer.baseclass import BaseClass
from rule_ye import solution
from bs4 import BeautifulSoup
from rule_ye import GetHTMLText,GetTitleUrl,GetContent,GetWebsite,GetKeyWords,\
    GetImg2md5,GetClassify,GetDate,GetImgUrl,GetSource,GetTitle,GetUrl2md5,GetAuthor
from rule_ye import solution1


class cnii(BaseClass):
    def __init__(self,url_md5 = None,content = None,url = None):
        super(BaseClass,self).__init__()
        self.url_md5 = url_md5
        self.title_url = url
        self.content = content
        self.analyse_rule = {
            'GetTitle': ['.content h1','body h3'],
            'GetDate': ['.conzz','.sm_q'],
            'GetSource': ['.conzz','aut','中国信息产业网'],
            'GetClassify': ['.dq','.dqwz_q'],
            'GetContent': ['.conzw','.zwnr_q'],
            'GetImgUrl': ['.conzw','.zwnr_q'],
            'GetWebsite': '中国信息产业网',
            'GetKeyWords': None,
            'GetAuthor': ['.aut','.conzz','编辑']
        }

    def analyze(self):
        return solution(self.url_md5,self.title_url,self.content,self.analyse_rule)

if __name__ == '__main__':
    url = "http://www.cnii.com.cn/yy/content/2012-11/05/content_1016699.htm"
    soup = BeautifulSoup(GetHTMLText(url), 'html.parser')
    a = cnii()
    # print(GetDate(soup,a.analyse_rule['GetDate']))
    #print(solution1('1', url, a.analyse_rule))
    #print(GetKeyWords(soup, a.analyse_rule["GetKeyWords"]))
    print(GetAuthor(soup,a.analyse_rule['GetAuthor']))