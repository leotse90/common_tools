#coding=utf-8

'''
Tools for get information of server.

@author: LeoTse
'''
import os
import socket

def cpu_load_info():
    '''
    /proc/loadavg:
    1.60 1.49 1.56 1/8100 24998
    
    The first three columns measure CPU and IO utilization of the last one, five, and 10 minute periods. 
    The fourth column shows the number of currently running processes and the total number of processes. 
    The last column displays the last process ID used.
    '''
    load_info_dict = {}
    with open("/proc/loadavg", "r") as f:
        info = f.read().split()
        load_info_dict["Lavg_1"] = float(info[0])
        load_info_dict["Lavg_5"] = float(info[1])
        load_info_dict["Lavg_15"] = float(info[2])
        load_info_dict["Nr"] = info[3]
        load_info_dict["Last_pid"] = int(info[4])

    return load_info_dict

def mem_info():
    '''
    /proc/meminfo:
    MemTotal:       131989500 kB
    MemFree:          720196 kB
    Buffers:         3834844 kB
    Cached:         40816752 kB
    SwapCached:       638056 kB
    Active:         66954704 kB
    ...
    '''
    mem_info_dict = {}
    with open("/proc/meminfo") as f:
        for line in f.readlines():
            key = line.split(":")[0]
            value = line.split(":")[1].split()[0]
            mem_info_dict[key] = float(value)
    
    mem_info_dict["MemUsed"] = mem_info_dict['MemTotal'] - mem_info_dict['MemFree'] - mem_info_dict['Buffers'] - mem_info_dict['Cached']
    mem_info_dict["Used_Per"] = round((mem_info_dict['MemUsed']) / (mem_info_dict['MemTotal']), 5)
    
    return mem_info_dict

def disk_info():
    disk_info_dict = {}
    dinfo = os.statvfs("/")
    disk_info_dict["Available"] = dinfo.f_bsize * dinfo.f_bavail
    disk_info_dict["Capacity"] = dinfo.f_bsize * dinfo.f_blocks
    disk_info_dict["Used"] = dinfo.f_bsize * dinfo.f_bfree
    disk_info_dict["Avai_per"] = dinfo.f_bavail / dinfo.f_blocks
    
    return disk_info_dict
    
def port_available(ip, port):
    try:
        sc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sc.settimeout(2) # timeout
        sc.connect((ip, port))
        sc.close()
        return True
    except:
        sc.close()
        return False
    