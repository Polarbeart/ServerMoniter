import sqlite3
import os
import time

class sqlClass(object):
    def __new__(cls):
        if not hasattr(cls,'instance'):
            cls.instance = super(sqlClass,cls).__new__(cls)
        return cls.instance
    def __init__(self):
        self.createSysInfo()


    # DES:FIELDS DESCRIPTION
    # IP
    # cpuCount,cpuUsed
    # memoryTotal,memoryInfo,memoryUsedSize,memoryUsed
    # net,bytesRcvd,bytesSent,realTimeRcvd,realTimeSent,TIM
    def createSysInfo(self):
        logDB = 'test2_stand.db'
        sqlpath = (os.path.dirname(os.path.realpath(__file__)))
        if logDB in os.listdir(sqlpath):
            self.con = sqlite3.connect(os.path.join(sqlpath, logDB), check_same_thread=False)
        else:
            self.con =sqlite3.connect(os.path.join(sqlpath,logDB),check_same_thread=False)
            self.con.execute('''CREATE TABLE SYSTEMINFO
                (IP                TEXT,
                cpuCount           TEXT,
                cpuUsed            INTEGER,
                memoryTotal        TEXT,
                memoryInfo         TEXT,
                memoryUsedSize     TEXT,
                memoryUsed         INTEGER,
                net                TEXT,
                bytesRcvd          TEXT,
                bytesSent          TEXT,
                realTimeRcvd       TEXT,
                realTimeSent       TEXT,
                TIM                INTEGER
                );''')
            self.con.execute('''CREATE TABLE PROGRESS 
                (IP            TEXT,
                PRONAME        TEXT,
                MEMUSED        INTEGER,
                STATE          TEXT,
                STARTTIME      INTEGER,
                PORT           TEXT,
                TIM            INTEGER
                );''')


    # 录入服务器基本信息
    def insertInfo(self,info):
        self.con.execute("INSERT INTO SYSTEMINFO (IP,cpuCount,cpuUsed,memoryTotal,memoryInfo,"
                         "memoryUsedSize,memoryUsed,net,bytesRcvd,bytesSent,realTimeRcvd,realTimeSent,TIM) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)",
                         ('test1',info[1],info[2],info[3],info[4],info[5],info[6],
                                    info[7],info[8],info[9],info[10],info[11],info[12]))
        self.con.commit()
        print("SYSTEMINFO TABLE HAS SAVED")

    # 录入进程详细信息
    def insert_pro(self,info):
        self.con.execute("INSERT INTO PROGRESS (IP,PRONAME,MEMUSED,STATE,STARTTIME,PORT) VALUES ("
                         "?,?,?,?,?,?)", ('test1',info[1],info[2],info[3],info[4],'null'))
        self.con.commit()
        print("PROGRESS TABLE HAS SAVED")

    # 获取当前时间
    def getTime(self):
        return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    # 查询相关IP系统信息
    def selectInfo(self,IP):
        try:
            res = self.con.execute("SELECT * FROM SYSTEMINFO WHERE IP =(?)",(IP,)).fetchall()
            print(len(res))
            result = [True,res]
        except Exception as e:
            result = [False,str(e)]


        return result

    # 查询相关IP的进程信息
    def select_pro(self,IP):
        try:
            res = self.con.execute("SELECT * FROM PROGRESS WHERE IP =(?)",(IP,)).fetchall()
            result = [True,res]
        except Exception as e:
            result = [False,str(e)]
        return result

    # 自定义查询信息
    def define_self(self,sql):
        try:
            res = self.con.execute(sql).fetchall()
            print(len(res))
            result = [True, res]
            print("define_self select is executed!")
        except Exception as e:
            result = [False, str(e)]

        return result
    # 自定义删除信息
    def define_del(self,sql):
        try:
            self.con.execute(sql)
            self.con.commit()
            print("define_del has executed!")
        except Exception as e:
            print(e)


    # 根据IP查询时间



# -----------Abandond Test--------------#
    def queryall(self, sql):
        """
        查询所有的数据及对应的列名
        :param sql:
        :return:
        """
        self.cur.execute(sql)
        # TODO 获取查询结果的列名
        columns_tuple = self.cur.description
        # columns_tuple示例： (('TACHE_NAME', None, None, None, None, None, None), ('avgtime', None, None, None, None, None, None), ('DATE', None, None, None, None, None, None), ('ANALYSIS_TIME', None, None, None, None, None, None))
        columns_list = [field_tuple[0] for field_tuple in columns_tuple]
        # TODO 获取查询结果
        query_result = self.cur.fetchall()
        return query_result, columns_list

    # 传入sql语句查询内容
    # def get_db():
    #     db = sqlite3.connect('Goods.db')
    #     db.row_factory = sqlite3.Row
    #     return db
    # def query_db(query, args=(), one=False):
    #     db = get_db()
    #     cur = db.execute(query, args)
    #     db.commit()
    #     rv = cur.fetchall()
    #     db.close()
    #     return (rv[0] if rv else None) if one else rv
