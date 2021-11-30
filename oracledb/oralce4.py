# -*- coding:utf-8 -*-
# !/usr/bin/env python
# @Author  :PolarBear
# @DES     :任务调度模块，定时存储sqlite,处理前端请求
# @DATE    :2021.11.17


import  cx_Oracle
from sys import modules


key = 'isctest02/Star*2019#@192.168.11.96:11521/orcl'
#连接Oracle数据库
class oracleOperation():

    def __init__(self):
        self.createSysInfo()

    def createSysInfo(self):
        # db = oracleOperation()


        # 验证table
        bool = self.verify_table('SYSTEMINFO')
        if bool ==0:
            connection = self.openOracleConn()
            cursor = connection.cursor()
            #执行SQL,创建一个表
            cursor.execute("""CREATE TABLE SYSTEMINFO
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
                            TIM                NUMBER,
                            TIME               CHAR(10)
                            )""")
            cursor.execute("""CREATE TABLE PROGRESS
                           (IP            VARCHAR2(15),
                           PRONAME        VARCHAR2(100),
                           MEMUSED        NUMBER,
                           STATE          VARCHAR2(10),
                           STARTTIME      VARCHAR2(20),
                           PORT           NUMBER,
                           TIM            TIMESTAMP,
                           TIME           CHAR(21)
                            )""")
            # 提交该表
            connection.commit()

            print("Table has Created!")
        else:
            # 另外创建连接
            print('Table has Existed!')
        # 关闭连接，释放资源
        # self.cursor.close()
        # print('已经关闭数据库')
    # 验证数据库是否有该表
    def verify_table(self, table):
        connection = self.openOracleConn()
        cursor = connection.cursor()
        sql = "select count(*) from user_tables where table_name =upper('" + table + "')"
        cursor.execute(sql)
        one = cursor.fetchone()
        print(one[0])
        # print(res)
        return one[0]


    def openOracleConn(self):
        #建立Oracle远程连接
        highway=cx_Oracle.connect(key)
        #获取cursor指针
        return highway

    # 自定义查询语句
    def define_self(self,sql):
        connection = self.openOracleConn()
        cursor = connection.cursor()
        # 数据库操作
        # 1.查询
        # sql = 'select * from systeminfo'
        result = cursor.execute(sql)
        print('type of result', type(result))  # 获取使用cursor对象的execute的方法返回的对象的类型
        print('result:', result)  # 获取使用cursor对象的execute的方法返回的对象
        print("Number of rows returned: %d" % cursor.rowcount)
        rows = cursor.fetchall()  # 得到所有数据集

        print("rows:", rows)  # fetchall（）方法得到的到底是设么类型的对象

        # for i in rows:
        #     print('IP：', i[0])
        #     print('CPU_COUNT：', i[1])
        #     print('CPU_USED：', i[2])
        cursor.close()
        connection.close()
        return rows


    # 指定IP 查询
    def selectInfo(self, IP):
        connection = self.openOracleConn()
        cursor = connection.cursor()
        # 数据库操作
        # 1.查询
        sql = "select * from systeminfo where ip = '"+IP+"'"
        print(sql)
        result = cursor.execute(sql)
        rows = cursor.fetchall()  # 得到所有数据集
        print("rows:", rows)
        cursor.close()
        connection.close()
        return rows

    # 根据IP查询进程信息
    def select_pro(self, IP):
        connection = self.openOracleConn()
        cursor = connection.cursor()
        # 数据库操作
        # 1.查询
        sql = "select * from progress where ip = '" + IP + "'"
        print(sql)
        result = cursor.execute(sql)
        rows = cursor.fetchall()  # 得到所有数据集
        print("rows:", rows)
        cursor.close()
        connection.close()

        return rows


    # 自定义删除信息
    def define_del(self, sql):
        connection = self.openOracleConn()
        cursor = connection.cursor()
        print(sql)
        cursor.execute(sql)
        print("已清除之前的进程信息")
        connection.commit()
        cursor.close()
        connection.close()

    # 插入服务器的相关数据
    def insertInfo(self, info):
        connection = self.openOracleConn()
        cursor = connection.cursor()
        # 数据库操作
        cursor.execute("INSERT INTO SYSTEMINFO (IP,cpuCount,cpuUsed,memoryTotal,memoryInfo,"
                            "memoryUsedSize,memoryUsed,net,bytesRcvd,bytesSent,realTimeRcvd,realTimeSent,TIM,TIME) VALUES (:1,:2,:3,:4,:5,:6,:7,:8,:9,:10,:11,:12,:13,:14)",info)
        print("SYSTEMINFO TABLE HAS SAVED")
        connection.commit()
        print("已经提交系统信息！")
        cursor.close()
        connection.close()

    # 录入进程详细信息
    def insert_pro(self, info):
        connection = self.openOracleConn()
        cursor = connection.cursor()
        cursor.execute(
            "INSERT INTO PROGRESS (IP,PRONAME,MEMUSED,STATE,TIME,PORT) VALUES(:1,:2,:3,:4,:5,:6)", info)
        connection.commit()
        print("已经提交进程信息！")
        print("PROGRESS TABLE HAS SAVED")



if __name__ == '__main__':
    db = oracleOperation()
    connection = db.openOracleConn()
    sql = "select * from systeminfo"
    # 能运行的无条件查询语句
    # db.select_difine(connection,sql)

    # 指定IP进行查询系统信息
    # db.selectInfo('192.168.103.163')

    # 指定IP 进行查询进程信息
    db.select_pro('192.168.103.163')
