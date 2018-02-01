import os
import time
import logging
import re
import rule_ye

from DataHelper import DataHelperr
from analyzer.xiancn_com import xian
from analyzer.ylxw_com_cn import ylxw
from analyzer.chinaqw_com import chinaqw
from analyzer.chinawater_com_cn import  chinawater
from analyzer.cnii_com_cn import cnii
from analyzer.cz001_com_cn import cz001
from analyzer.wenming_cn import wenming
from analyzer.stdaily_com import stdaily
from analyzer.sxdaily_com_cn import sxdaily
from analyzer.nxnet_cn import nxnet
from analyzer.online_sh_cn import online_sh
from analyzer.xinjiangnet_com import xinjiangnet
from analyzer.yznews_com_cn import  yznews


#EXCUTE_SQL = "SELECT top %s id, data,url from %s "
EXCUTE_SQL = "SELECT top %s id, data, url from %s where [index] >= %s"
#EXCUTE_SQL  = "SELECT top %s id, data,url from %s where url='http://www.chinaqw.com/node2/node2796/node3264/node3468/node3606/node3609/userobject6ai257031.html'"
#  _const.EXCUTE_SQL = "SELECT top 100* from %s"

# 传入为表名
def test_start(table_name, fetch_num,start_id):
    # 1.获取数据库操作 cur
    ddddd = DataHelperr()
    #conn = ddddd.getConn("192.168.2.197", "huangqian", "huangqian@pass", "blackhole_data")
    conn = ddddd.getConn("192.168.2.197", "huangqian", "huangqian@pass","blackhole_data")
    # conn = DataHelper.getConn("127.0.0.1","sa", "123456", "DB_Fulltext_Newspaper_Scrapy")
    cur = conn.cursor()

    #log = LogFile(os.path.join(os.getcwd(), "log_%s.txt" % time.time() ), logging.INFO)

    # 2.初始化解析器
    #parsers = init_parsers()
    # 获取需要的解析器
    #parser = parsers[table_name]

    # 3.获取待解析的数据
    sql = EXCUTE_SQL %(fetch_num, table_name,start_id)
    cur.execute(sql)
    table_list = cur.fetchall()

    # 4.解析数据
    count = 0
    count1 = 0
    website_name=""
    for each_tuple in table_list:
        # 传入参数顺序应该为 url_md5  content  title
        #test = xian(each_tuple[0], each_tuple[1], each_tuple[2])
        #test = ylxw(each_tuple[0], each_tuple[1], each_tuple[2])
        #test = chinaqw(each_tuple[0], each_tuple[1], each_tuple[2])
        #test = chinawater(each_tuple[0], each_tuple[1], each_tuple[2])
        #test = cnii(each_tuple[0], each_tuple[1], each_tuple[2])
        #test = cz001(each_tuple[0], each_tuple[1], each_tuple[2])
        #test = wenming(each_tuple[0], each_tuple[1], each_tuple[2])
        #test = stdaily(each_tuple[0], each_tuple[1], each_tuple[2])
        #test = sxdaily(each_tuple[0], each_tuple[1], each_tuple[2])
        #test = nxnet(each_tuple[0], each_tuple[1], each_tuple[2])
        #test = xinjiangnet(each_tuple[0], each_tuple[1], each_tuple[2])
        test = yznews(each_tuple[0], each_tuple[1], each_tuple[2])
        #print('each[2]',each_tuple[2])
        if each_tuple[2].find("bbs") >=0 or each_tuple[2].find("blog") >=0: continue
        print(each_tuple[2])
        item = test.analyze()
        count1 += 1
        if item:
            count +=1
            print("解析的内容：%s,%s,%s,%s,%s,%s" %(item[1], item[2], item[3],item[4],item[9],item[12]))
        else:
            # log.WriteLog("解析失败的url:%s" % each_tuple[2])
            print("解析失败的url:%s" % each_tuple[2])
    if count1 == 0 : print('测试数据全部是bbs论坛')
    else : print("测试[%s]条解析成功的比例为[%.2f]" %(count1, count/count1) )
    # 5.释放资源关闭数据库连接
    DataHelperr.closeConn(conn)

if __name__ == '__main__':
    #test_start("chinaqw_com",1000,0)
    #test_start("ylxw_com_cn",500,0)
    #test_start("xiancn_com",5000,0)
    #test_start("sxdaily_com_cn",1000,0)
    #test_start("chinawater_com_cn",500,0)
    #test_start("cnii_com_cn",1000,0)
    #test_start("cz001_com_cn",1000,0)
    #test_start("stdaily_com",1000,0)
    #test_start("nxnet_cn",500,0)
    #test_start("xinjiangnet_com",1000,0)
    test_start("yznews_com_cn",1000,0)

