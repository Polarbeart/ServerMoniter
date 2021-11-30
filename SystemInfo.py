import psutil
import time
# from sqlitedb.sqlitedb import sqlClass
from oracledb.oralce4 import oracleOperation
from datetime import datetime
import socket
sql = oracleOperation()
list_info = []
dt = datetime.now()
# 自调节参数：flag 查询进程函数标识
#####################
flag = True

#####################
def SysInfo(flag):



    # 获取本机IP
    ip = get_host_ip()
    # ip ='172.17.190.229'
    # CPU信息
    print("=============CPU信息=============")
    cpuUsed = psutil.cpu_percent(1)
    cpuCount = psutil.cpu_count(logical=False)
    print("cpuCount:"+str(cpuCount)+"\ncpuUsed:"+str(cpuUsed))
    # 内存信息
    print("=============内存信息=============")
    memoryTotal = round(psutil.virtual_memory().total/(1024.0*1024.0*1024.0), 2)
    memoryInfo = psutil.virtual_memory()
    memoryUsedSize = round(memoryInfo.used / (1024.0 * 1024.0 * 1024.0), 2)
    memoryUsed = round(memoryUsedSize / memoryTotal, 2) * 100
    # memoryUsed = round(memoryUsedSize / memoryTotal, 2)
    print("memoryTotal:"+str(memoryTotal)+"\nmemoryInfo:"+str(memoryInfo)+
          "\nmemoryUsedSize:"+str(memoryUsedSize)+"\nmemoryUsed:"+str(memoryUsed))
    # 网络io
    print("=============IO信息=============")
    net = psutil.net_io_counters()
    bytesRcvd = (net.bytes_recv / 1024)
    bytesSent = (net.bytes_sent / 1024)
    time.sleep(1)
    net = psutil.net_io_counters()
    realTimeRcvd = round(((net.bytes_recv / 1024) - bytesRcvd), 2)
    realTimeSent = round(((net.bytes_sent / 1024) - bytesSent), 2)
    times = time.strftime('%H:%M:%S', time.localtime())
    tim = time.time()
    print("net:"+str(net)+"\nbytesRcvd:"+str(bytesRcvd)+
          "\nbytesSent:"+str(bytesSent)+"\nrealTimeRcvd:"+str(realTimeRcvd)
          +"\nrealTimeSent:"+str(realTimeSent)+"\ntim:"+str(dt))
    list_info= [ip,cpuCount,cpuUsed,str(memoryTotal),str(memoryInfo),str(memoryUsedSize),str(memoryUsed),str(net),str(bytesRcvd),
                str(bytesSent),str(realTimeRcvd),str(realTimeSent),tim,times]  #13
    ## 是否进行查询进程信息函数，
    ## 参数：flag，默认flase
    if flag:
        get_pro(ip)

    # print(alist)

    ## 向sqlite 录入信息

    # print(type(tim))
    sql.insertInfo(info = list_info)
    # res = sql.select_pro('test1')
    # res2 = sql.selectInfo('test1')
    # print(res2)

# 根据pid寻找该进程的端口
alist = []
def netpidport(pid: int):
    # 获取当前的网络连接信息
    net_con = psutil.net_connections()
    for con_info in net_con:
        if con_info.pid == pid:
            alist.append({pid:con_info.laddr.port})
    # return alist

# 获取本机ip
def get_host_ip():
    try:
        s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        s.connect(('10.0.0.1',8080))
        ip= s.getsockname()[0]
    finally:
        s.close()
    return ip


def select_self():
    sql1 = "select * from SYSTEMINFO where ip = 'test1'"
    res = sql.define_self(sql1)
    print(res)

# 获取server进程信息
def get_pro(ip1):
    # 先将原始的进程信息清除
    ip = get_host_ip()
    sql_del = "delete from progress where ip = '"+ip+"'"
    sql.define_del(sql_del)
    # 查看系统全部进程
    print("=============进程信息=============")

    for pnum in psutil.pids():
        netpidport(pnum)
        p = psutil.Process(pnum)
        tim_start = datetime.fromtimestamp(p.create_time()).strftime("%Y-%m-%d %H:%M:%S")
        print(u"进程名 %-20s  内存利用率 %-16s 进程状态 %-10s 创建时间 %-10s " \
              % (p.name(), round(p.memory_percent(),4), p.status(), p.create_time()))
        list_pro = [ip, str(p.name()), round(p.memory_percent(),4), str(p.status()),tim_start,'1234']
        print(p.create_time())


        # 将获取到的进程信息存入数据库
        sql.insert_pro(info=list_pro)
    print("当前进程数量: " + str(len(psutil.pids())))
    print("端口数量" + str(len(alist)))


if __name__ == '__main__':
    SysInfo(flag)


# ---debug
#     get_pro('1')
    # select_self()