from analyzer.baseclass import BaseClass
from rule_ye import solution
from bs4 import BeautifulSoup
from rule_ye import GetHTMLText,GetTitleUrl,GetContent,GetWebsite,GetKeyWords,GetImg2md5,\
    GetClassify,GetDate,GetImgUrl,GetSource,GetTitle,GetUrl2md5,GetAuthor
from rule_ye import solution1

class cz001(BaseClass):
    def __init__(self,url_md5 = None,content = None,url = None):
        super(BaseClass,self).__init__()
        self.url_md5 = url_md5
        self.title_url = url
        self.content = content
        self.analyse_rule = {
            'GetTitle': ['h1.orange.dtitle','.title','#title p strong','header h1'],
            'GetDate': ['.dinfo','.info','#title','header em'],
            'GetSource': ['.dinfo','.info','中国常州网'],
            'GetClassify': ['.channeltitlecrumbs','#newstitle'],
            'GetContent': ['#zoom','.contentbox','.content','.articleMain','#contentwarp','.info_detail'],
            'GetImgUrl': ['#zoom','.contentbox','.content','.articleMain','#contentwarp','.info_detail'],
            'GetWebsite': '中国常州网',
            'GetKeyWords': None,
            'GetAuthor': ['editors','editor','.dinfo','编辑']
        }

    def analyze(self):
        return solution(self.url_md5,self.title_url,self.content,self.analyse_rule)

if __name__ == '__main__':
    url = "http://cznews.cz001.com.cn/html/wap/detail.php?pid=16642323"
    soup = BeautifulSoup(GetHTMLText(url), 'html.parser')
    a = cz001()
    # print(GetDate(soup,a.analyse_rule['GetDate']))
    print(solution1('1', url, a.analyse_rule))
    print(GetAuthor(soup,a.analyse_rule["GetAuthor"]))