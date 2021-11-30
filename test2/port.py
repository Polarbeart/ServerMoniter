# python根据pid寻找端口
import psutil


def netpidport(pid: int):
    """根据pid寻找该进程对应的端口"""
    alist = []
    # 获取当前的网络连接信息
    net_con = psutil.net_connections()
    for con_info in net_con:
        if con_info.pid == pid:
            alist.append({pid:con_info.laddr.port})
    return alist


def netportpid(port: int):
    """根据端口寻找该进程对应的pid"""
    adict = {}
    # 获取当前的网络连接信息
    net_con = psutil.net_connections()
    for con_info in net_con:
        if con_info.laddr.port == port:
            adict[port] = con_info.pid
    return adict


if __name__ == '__main__':
    print(netpidport(3306))
    print(netportpid(3389))

