import  cx_Oracle
from sys import modules
import unittest

key = 'isctest01/Star*2019#@192.168.11.96:11521/orcl'
#连接Oracle数据库
class oracleOperation():
    def openOracleConn(self):
        #建立Oracle远程连接
        highway=cx_Oracle.connect(key)
        #获取cursor指针
        return highway


    def select(self,connection):
        cursor = connection.cursor()
        # 数据库操作
        # 1.查询
        sql = 'select * from systeminfo'
        result = cursor.execute(sql)
        print('type of result', type(result))  # 获取使用cursor对象的execute的方法返回的对象的类型
        print('result:', result)  # 获取使用cursor对象的execute的方法返回的对象
        print("Number of rows returned: %d" % cursor.rowcount)
        rows = cursor.fetchall()  # 得到所有数据集

        print("rows:", rows)  # fetchall（）方法得到的到底是设么类型的对象
        #
        # for i in rows:
        #     print('序号：', i[0])
        #     print('水果种类：', i[1])
        #     print('水果库存量：', i[2])
        cursor.close()
        connection.close()





        #1.插入操作
    def factorSelect (self,connection,param):
        cursor=connection.cursor()
        # 带参数的查询  ，例子如下：
        #query1 = cursor.execute('SELECT * FROM employees  WHERE  department_id =:dept_id AND salary >: sal', named_params)
        sql='select * from Python_Oracle where  kinds =:kinds'
        query1 = cursor.execute(sql,param)  #特别的注意，具体 的条件查询的格式
        row=cursor.fetchall()
        print(row)

        cursor.close()
        connection.close()
    pass

    def insert(self,connection):
        cursor=connection.cursor()
        sql="insert into Python_Oracle (id,kinds,numbers) values (:id,:kinds,:numbers)"
        cursor.prepare(sql)

       #2,'西瓜','100kg'
        xx=[{'id':6},{'kinds':'荔枝'},{'numbers':'100kg'}]
        # result=cursor.execute(None,{'id':6,'kinds':'荔枝','numbers':'100kg'})
        # result=cursor.execute(None,xx)
        result=cursor.execute(None,xx)

        print("Insert result:",result)

        connection.commit()

        cursor.close()
        connection.close()
    pass


    def insert2(self,connection,insertParam=[]):
        cursor=connection.cursor()
        # M=[(11,'sa','sa'),]
        sql="insert into Python_Oracle (id,kinds,numbers) values (:id,:kinds,:numbers)"
        if(len(insertParam)==0):
            print("插入的数据行的参数不能为空！")
        else:
            cursor.prepare(sql)
            result=cursor.executemany(None,insertParam)

            print("Insert result:",result)
            # count=cursor.execute("SELECT COUNT(*) FROM python_modules")
            # print("count of python_modules:",count)

        connection.commit()

        cursor.close()
        connection.close()
    pass

    def insert3(self,connection):
        cursor=connection.cursor()
        M = []
        for m_name, m_info in modules.items():
            try:
                M.append((m_name, m_info.__file__))
            except AttributeError:
                pass
        print("M",M)
        for item in M:
            print(item)
        sql = "INSERT INTO python_modules(module_name, file_path) VALUES (:1, :2)"

        cursor.prepare(sql)

        cursor.executemany(None, M)
        connection.commit()

        cursor.close()
        connection.close()
    pass

    #废弃方法。不能运行，但是不知道为什么！！！
    def test2(self,connection):
        oraDb=connection
        cursor = oraDb.cursor()

        create_table = """
        CREATE TABLE python_modules1 (
        module_name VARCHAR2(50) NOT NULL,
        file_path VARCHAR2(300) NOT NULL
        )
        """


        cursor.execute(create_table)
        M = []
        for m_name, m_info in modules.items():
            try:
                M.append((m_name, m_info.__file__))
            except AttributeError:
                pass
        print(M)
        sql = "INSERT INTO python_modules1(module_name, file_path) VALUES (:1, :2)"

        cursor.prepare(sql)

        cursor.executemany(None,M)
        cursor.execute("SELECT COUNT(*) FROM python_modules")
        connection.commit()
    pass
    def Delete(self,conn):
        cursor=conn.cursor()
        sql="delete "




pass

if __name__=='__main__':
    db = oracleOperation()
    connection=db.openOracleConn()

    #能运行的无条件查询语句
    db.select(connection)

    # #能够运行的条件查询语句
    # kinds_param = {'kinds': '芒果'}
    # # db.factorSelect(connection,kinds_param)
    #
    # #自己的能够运行的insert语句
    # insertParam=[(5,'大象','1T'),(6,'蚂蚁','0.001g')]
    # db.insert2(connection,insertParam)




##############################
    #第一个成功的运行的python-Oracle insert 语句       这个是参考网上的例子
    # db.insert3(connection)

    #不能运行的网上的insert例子
    # db.test2(connection)