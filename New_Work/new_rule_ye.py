#!/usr/bin/env python
#coding:utf-8

from DataHelper import DataHelperr
EXCUTE_SQL= 'insert into %s values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
class Crawler:
    def __init__(self):
        pass

    def find_all_url(self):
        pass

    def parse_body(self):
        pass

    def solve(self):
        pass

    def clean_word(sstr):  # 消除一段话中所有转义符号
        return "".join(sstr.split())

    def write_to_dbms(self,table_name=None,datas = None):
        '''
        :param table_name: 要写进数据库哪个表名
        :param datas:  如果赋参数后就说明是批量
        :return:
        '''
        dbms = DataHelperr()
        conn = DataHelperr.getConn('192.168.2.210','ye','ye@pass','fund')
        cur = conn.cursor()
        if datas == None : datas = self.solve()
        for index,data in enumerate(datas):
            try:
                sql = 'insert into '+table_name+' values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
                cur.execute(sql,data)
                #print('index:',index)
            except Exception as e:
                print('Error Information:什么鬼',e)
                print(data)
        conn.commit()
        return True

    def parse_body_find(self, soup, keyword):
        text = soup.text
        print('text',text)