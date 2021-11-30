import socket
def get_host_ip():
    try:
        s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        s.connect(('10.0.0.1',8080))
        ip= s.getsockname()[0]
    finally:
        s.close()
    return ip
if __name__=='__main__':
    LocalIP = get_host_ip()
    print ('LocalIP:%s' % LocalIP)