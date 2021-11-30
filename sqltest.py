# sqltest,this is a test file
#
from sqlitedb.sqlitedb import sqlClass
from oracledb.oradb import sqlClass
from app import get_txt_ip
import time
from datetime import datetime, timedelta

sql = sqlClass()

def select_time():
    sql_l1 = "select * from progress where ip = 'test1' "
    res = sql.define_self(sql_l1)
    for i in res[1]:
        print(i)



def more_info_pro():
    sql_1 = "select * from systeminfo where ip ='test1'"
    res = sql.define_self(sql_1)
    for i in res[1]:
        print(i[0])


def insert_test():
    sql.insertInfo()


# 获取平均负载
def get_load_avg():
    try:
        import subprocess
        tmp = subprocess.getstatusoutput('uptime')
        load_avg = tmp[-1].split(',')[-2].strip()
    except Exception as e:
        load_avg = 0
    print(load_avg)
    return load_avg


def get_1():
    sql_1 = "select tim from systeminfo where ip ='test1' order by tim desc limit 10"
    res = sql.define_self(sql_1)
    print(res)

def get_c1(ip_sub ='test1'):
    # sql_c1 = "select cpuUsed,memoryUsed from SYSTEMINFO where ip = 'test1' order by tim desc limit 1 "
    sql_c1 = "select * from SYSTEMINFO where ip = '" +ip_sub +"' order by tim desc limit 1 "
    print(sql_c1)
    res = sql.define_self(sql_c1)
    print(res[1])
    # for i in res[1]:
    #     print(i[0])
    #     print(i[1])


def del_pro_info():
    sql_del = "delete  from PROGRESS where ip ='test1'"
    sql.define_del(sql_del)


def c1():
    sql_r1 = "select * from (select realTimeRcvd,realTimeSent,tim from SYSTEMINFO where ip = '192.168.103.163' order by tim desc) where rownum <37"

    res = sql.define_self(sql_r1)
    for i in res[1]:
        print(i[0])
        print(i[1])
        print(i[2])
        # realTimeRcvd.append(i[0])
        # realTimeSent.append(i[1])
        # time.append(i[2])


def select_te():
    # ip = 192.168.103.163''
   # sql2 = "select * from progress where ip ='192.168.103.163'"
    sql1 = 'select * from (select cpuused,tim from systeminfo order by tim desc) where rownum <5'
    # print(sql1)
    res= sql.define_self(sql1)
    content = res[1]
    for i in res[1]:
        print(i[1])
        tim = timeStamp(i[1])
        print(tim)
def gettime():
    # dtim = 44152.0146412037
    # dtim = 1637734322.6554823
    # print(type(dtim))
    # DateObj = datetime(year=1900, month=1, day=1)
    # DateObj += timedelta(days=dtim)  # 转换datetime格式，这里的datetime就是float，值为上面注释的
    # dateTime = DateObj.strftime("%H:%M:%S")
    # print(dateTime)

    #1637734322.6554823
    tim = time.strftime('%H:%M:%S',time.localtime(time.time()))



    print(tim)


 # 输入毫秒级的时间，转出正常格式的时间
def timeStamp(timeNum):
    timeStamp = float(timeNum / 1000)
    timeArray = time.localtime(timeStamp)
    otherStyleTime = time.strftime("%H:%M:%S", timeArray)
    return otherStyleTime


if __name__ == '__main__':
    # select_time()
    # more_info_pro()
    # get_load_avg()
    # get_c1()
    # del_pro_info()
    c1()
    # select_te()
    # timeStamp(1637734322.6554823)