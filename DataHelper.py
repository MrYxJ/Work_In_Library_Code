import sys,pymssql

class DataHelperr():
    # 获取数据库连接
    conn = None
    @classmethod
    def getConn(self,host, user, password,databse,try_time=None):
        try:
            if try_time == None : try_time =3
            cnt = 0
            while self.conn == None and cnt <=try_time:
                cnt +=1
                self.conn = pymssql.connect(host=host, user=user, password= password,database= databse, charset="utf8")
            return self.conn
        except Exception as e:
            print('Conn 连接失败')
            return None
    @classmethod
    def closeConn(self, conn):
       try:
            if conn:
                conn.close()
       except  Exception as e:
           pass



