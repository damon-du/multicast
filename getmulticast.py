'''
获取组播数据
'''
import struct
import time
import socket
import datetime

# 组播组IP和端口
mcast_group_ip = '229.0.0.11'
mcast_group_port = 9999
local_ip = '172.30.81.85'

# def cut(obj, sec):
#     return [obj[i:i + sec] for i in range(0, len(obj), sec)]


def receiver():
    # 建立接收socket，和正常UDP数据包没区别
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
    # 允许端口复用，看到很多教程都有没想清楚意义是什么，我这里直接注释掉
    # sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    # 获取本地IP地址
    # local_ip = socket.gethostbyname(socket.gethostname())
    # 监听端口，已测试过其实可以直接bind 0.0.0.0；但注意不要bind 127.0.0.1不然其他机器发的组播包就收不到了
    sock.bind((local_ip, mcast_group_port))
    # 加入组播组
    mreq = struct.pack("=4sl", socket.inet_aton(mcast_group_ip),
                       socket.INADDR_ANY)
    sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)
    # 下面的方法也可以加入组播组
    # status = sock.setsockopt(socket.IPPROTO_IP,
        # socket.IP_ADD_MEMBERSHIP,
        # socket.inet_aton(mcast_group_ip) + socket.inet_aton(local_ip));

    
    # 设置非阻塞，看到很多教程都有也没想清楚有什么用，我这里直接注释掉
    # sock.setblocking(0)
    while True:
        try:
            message, addr = sock.recvfrom(2048)
            print(message.hex().upper(),addr)
                
        except Exception as e:
            print(e)


if __name__ == "__main__":
    receiver()