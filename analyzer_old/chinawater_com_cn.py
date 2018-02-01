from analyzer.baseclass import BaseClass
from rule_ye import solution
from bs4 import BeautifulSoup
from rule_ye import GetHTMLText,GetTitleUrl,GetContent,GetWebsite,GetKeyWords,GetImg2md5,GetClassify,GetDate,GetImgUrl,GetSource,GetTitle,GetUrl2md5,GetAuthor
from rule_ye import solution1

class chinawater(BaseClass):
    def __init__(self,url_md5 = None,content = None,url = None):
        super(BaseClass,self).__init__()
        self.url_md5 = url_md5
        self.title_url = url
        self.content = content
        self.analyse_rule = {
            'GetTitle': ['.font11','.font16','td.font12','head title'],
            'GetDate': ['span strong','span[class="font9"]','.font10a'],
            'GetSource': ['中国水利网'],
            'GetClassify': ['.STYLE10'],
            'GetContent': ['.TRS_Editor','tr td[align="center"]','table[width="90%"]','td[valign="top"]'],
            'GetImgUrl': ['.TRS_Editor','td[align="left"]','table[width="90%"]','td[valign="top"]'],
            'GetWebsite': '中国水利网',
            'GetKeyWords': None,
            'GetAuthor': ['editors','editor','.Custom_UnionStyle p','编辑']
        }

    def analyze(self):
        return solution(self.url_md5,self.title_url,self.content,self.analyse_rule)


if __name__ == '__main__':
    url = "http://www.chinawater.com.cn/newscenter/2011jzzfwf/201801/t20180123_706056.html"
    soup = BeautifulSoup(GetHTMLText(url), 'html.parser')
    a = chinawater()
    #print(GetClassify(soup,a.analyse_rule['GetClassify']))
    #print(GetTitle(soup,a.analyse_rule['GetTitle']))
    #print(GetDate(soup,a.analyse_rule['GetDate']))
    #print(GetAuthor(soup,a.analyse_rule['GetAuthor']))
    print(solution1('1',url,a.analyse_rule))
    #print(GetSource(soup,a.analyse_rule['GetSource']))