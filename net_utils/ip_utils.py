#coding:utf8

'''
Tools for ip address operations.

@author:  LeoTse
'''

import socket
import struct

def ip2int(ip):
    if not ip:
        return 0
    return struct.unpack("!I", socket.inet_aton(ip))[0]

def int2ip(i):
    return socket.inet_ntoa(struct.pack("!I", i))

def ntoh(value):
    value = struct.pack('!I', value)
    return struct.unpack('I', value)[0]

def get_internet_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(('qq.com', 0))
    sockname = s.getsockname()
    return sockname[0]

def get_local_ip():
    return socket.gethostbyname(socket.gethostname())


if __name__ == '__main__':
    print int2ip(2015041500)
    print ip2int('121.14.11.89')