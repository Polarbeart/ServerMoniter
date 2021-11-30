# -*- coding:utf-8 -*-
# !/usr/bin/env python
# @Author  :PolarBear
# @DES     :任务调度模块，定时存储sqlite,处理前端请求
# @DATE    :2021.11.17

import cx_Oracle


#######临时配置文件######
#######################
key = 'isctest02/Star*2019#@192.168.11.96:11521/orcl'


#######################
class sqlClass(object):
    def __new__(cls):
        if not hasattr(cls,'instance'):
            cls.instance = super(sqlClass,cls).__new__(cls)
        return cls.instance
    def __init__(self):
        self.verify_table('SYSTEMINFO')
        # self.createSysInfo()

    # DES:FIELDS DESCRIPTION
    # IP
    # cpuCount,cpuUsed
    # memoryTotal,memoryInfo,memoryUsedSize,memoryUsed
    # net,bytesRcvd,bytesSent,realTimeRcvd,realTimeSent,TIM
    def createSysInfo(self):
        #执行SQL,创建一个表
        self.cursor.execute("""CREATE TABLE SYSTEMINFO
                        (IP                CHAR(15),
                        cpuCount           NUMBER,
                        cpuUsed            NUMBER,
                        memoryTotal        NUMBER,
                        memoryInfo         VARCHAR2(200),
                        memoryUsedSize     NUMBER,
                        memoryUsed         NUMBER,
                        net                VARCHAR2(200),
                        bytesRcvd          NUMBER,
                        bytesSent          NUMBER,
                        realTimeRcvd       NUMBER,
                        realTimeSent       NUMBER,
                        TIM                NUMBER
                        )""")
        self.cursor.execute("""CREATE TABLE PROGRESS
                       (IP            VARCHAR2(15),
                       PRONAME        VARCHAR2(100),
                       MEMUSED        NUMBER,
                       STATE          VARCHAR2(10),
                       STARTTIME      DATE,
                       PORT           NUMBER,
                       TIM            TIMESTAMP
                        )""")
        # 提交该表
        self.con.commit()

        print("Table has Created!")

    # 验证数据库是否有该表
    def verify_table(self,table):
        self.con = cx_Oracle.connect(key)
        self.cursor = self.con.cursor()
        sql = "select count(*) from user_tables where table_name =upper('"+table+"')"
        self.cursor.execute(sql)
        one = self.cursor.fetchone()
        print(one[0])
        # print(res)
        if one[0] == 0 :
            self.createSysInfo()
        else:
            print("THE table is exitd!")
        # return one[0]


    def insert_test(self,param):

        self.cursor.execute('insert into tb_user values(:id,:n,:p)', param)
        # 关闭连接，释放资源
        # 提交更改
        self.con.commit()

        # self.cursor.close()
        # print("已关闭游标")
        #
        # print("已经提交信息！")
        # self.con.close()
        # print('已经关闭数据库')
    # 插入服务器的相关数据
    def insertInfo(self, info):
        self.cursor.execute("INSERT INTO SYSTEMINFO (IP,cpuCount,cpuUsed,memoryTotal,memoryInfo,"
                            "memoryUsedSize,memoryUsed,net,bytesRcvd,bytesSent,realTimeRcvd,realTimeSent,TIM) VALUES (:1,:2,:3,:4,:5,:6,:7,:8,:9,:10,:11,:12,:13)",info)
        print("SYSTEMINFO TABLE HAS SAVED")
        self.con.commit()
        print("已经提交信息！")

    # 录入进程详细信息
    def insert_pro(self, info):
        self.cursor.execute("INSERT INTO PROGRESS (IP,PRONAME,MEMUSED,STATE,STARTTIME,PORT) VALUES(:1,:2,:3,:4,:5,:6)",info)
        self.con.commit()
        print("已经提交信息！")
        print("PROGRESS TABLE HAS SAVED")

    # # 查询相关IP系统信息
    def selectInfo(self, IP):
        try:
            sql = "SELECT * FROM SYSTEMINFO WHERE IP =("+IP+")"
            print(sql)
            self.cursor.execute(sql)
            res = self.cursor.fetchall()
            # for i in res:
            #     print(i[-1])
            result = [True, res]
        except Exception as e:
            result = [False, str(e)]

        return result

    # # 查询相关IP的进程信息
    def select_pro(self, IP):
        try:
            sql = "SELECT * FROM PROGRESS WHERE IP =("+IP+")"
            print(sql)
            self.cursor.execute(sql)
            res = self.cursor.fetchall()
            result = [True, res]
        except Exception as e:
            result = [False, str(e)]
        return result

    # 自定义查询信息
    def define_self(self, sql):
        try:
            print(sql)
            self.cursor.execute(sql)
            res = self.cursor.fetchall()
            result = [True, res]
            print("define_self select is executed!")
        except Exception as e:
            result = [False, str(e)]

        return result



# 自定义删除信息
    def define_del(self, sql):
        try:
            self.cursor.execute(sql)
            self.con.commit()
            print("已经提交信息！")
            print("define_del has executed!")
        except Exception as e:
            print(e)



