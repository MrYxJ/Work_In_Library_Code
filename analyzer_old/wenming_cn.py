from analyzer.baseclass import BaseClass
from rule_ye import solution
from bs4 import BeautifulSoup
from rule_ye import GetHTMLText,GetTitleUrl,GetContent,GetWebsite,GetKeyWords,GetImg2md5,GetClassify,GetDate,GetImgUrl,GetSource,GetTitle,GetUrl2md5
from rule_ye import solution1

class wenming(BaseClass):
    def __init__(self,url_md5 = None,content = None,url = None):
        super(BaseClass,self).__init__()
        self.url_md5 = url_md5
        self.title_url = url
        self.content = content
        self.analyse_rule = {
            'GetTitle': ['.tt-tit','#title_tex','.dc-title','.trs_title','.detail-title',
                         '.nr_left_bt','div[align="center"]','#ImgListLeft h3','strong',
                         '.artbox h3','#text_list div','#article h1','.content_title h1',
                         '.cloum-box03','p[align="center"] b','#xilan_con h1','.news-content h1',
                         '.article_tit','.ad-xingming','.wzy_top h1','.ynwmwshow_title h4',
                         '.text_title','.tzw01.fm01.fs22.text-333.lh40','.news h1','.infoTitle',
                         '.list-l h1','.newstitle'],
            'GetDate': ['.tt-rq','#time_tex','.dc-title02','.time_tex','.detail-canshu share h2',
                        '.nr_left_ly','div[align="right"]','#TextContentUL01','.function_tex label',
                        '#time','.content_title h2','p[align="center"]','.fubiao','.article_tit02',
                        '.ad-shijian','.wzy_top p','.ynwmwshow_title h6','.text_date','.time',
                        '#info_released_dtime','.list-l p','.border08.border09'],
            'GetSource': ['.tt-ly','#time_tex','.time_tex','#TextContentUL01','.function_tex',
                          '#time_left span','.article_tit02','.ynwmwshow_title h6','.from',
                          '#info_source','.border08.border09','中国文明网'],
            'GetClassify': ['.pl-t','.title','.bn','.location.border-btm-none h3',
                            '.lm_left_dh','#ImgListLeft h2'],
            'GetContent': ['.article','.TRS_Editor','.dc-text02','#zoom','.content_txt'],
            'GetImgUrl':  ['.article','.TRS_Editor','.dc-text02','#zoom','.content_txt'],
            'GetWebsite': '中国文明网',
        }

    def analyze(self):
        return solution(self.url_md5,self.title_url,self.content,self.analyse_rule)

if __name__ == '__main__':
    url = "http://cq.wenming.cn/wmbb/201608/t20160815_3594324.shtml"
    soup = BeautifulSoup(GetHTMLText(url), 'html.parser')
    a = wenming()
    #print(GetClassify(soup,a.analyse_rule['GetClassify']))
    #print(GetTitle(soup,a.analyse_rule['GetTitle']))
    #print(GetDate(soup,a.analyse_rule['GetDate']))
    #print(GetSource(soup,a.analyse_rule['GetSource']))
    #print(GetContent(soup,a.analyse_rule['GetContent'],url))
    print(solution1('1', url, a.analyse_rule))