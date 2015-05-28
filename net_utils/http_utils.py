#coding:utf8

'''
Tools for Http request and response.

@author: LeoTse
'''

import os
import urllib
import urllib2
import httplib

'''
Call GET method API and return the response.

@param server_conf:format {"gateway":"gateway info"}
@param params:format [("param1", "value1"), ("param2", "value2"), ...] 
'''
def invoke_get_api(server_conf, api, params):
    # url example: http://192.168.9.245/videos?id=0&hash="acxd23asd2dafpiojufdufhiqofqo"
    gateway = server_conf["gateway"]
    params_str = "&".join(["=".join(e) for e in params])
    
    # you can use below but sometimes it can't work when data is too long.
#     url = "http://{gateway}/{api}?{params_str}".format(gateway=gateway, api=api, params_str=params_str)
#     req = urllib2.Request(url)    
#     rep = urllib2.urlopen(req)
#     res = rep.read()
    
    ip_addr, port = gateway.split(":")
    http_conn = httplib.HTTPConnection(ip_addr, port)
    http_conn.request("GET", "/{api}?{params_str}".format(api=api, params_str=params_str))
    res = http_conn.getresponse().read()
    
    return res
    
'''
Call POST method API and return the response.

@param server_conf:format {"gateway":"gateway info"}
@param post_data:format {"key1":"value1","key2":"value2", ...} 
'''
def invoke_post_api(server_conf, api, post_data):
    # url
    gateway = server_conf["gateway"]
    post_data_urlencode = urllib.urlencode(post_data)

    url = "http://{gateway}/{api}".format(gateway=gateway, api=api)
    req = urllib2.Request(url=url, data=post_data_urlencode)
    rep = urllib2.urlopen(req)
    res = rep.read()

    return res

'''
Download file from given url and store it in given path.
'''
def download_file_by_url(file_url, file_name, file_store_path):
    # example:
    # wget -O /home/leotse/test/test.mp4 \
    # http://192.168.9.230:9096/group1/M00/00/00/wKgJ51VasR6AdCYSAI58WC-SRBw304.mp4
    file_path = os.path.join(file_store_path, file_name)
    ret = os.system("wget -O {dst_path} {src_url}".format(dst_path=file_path, src_url=file_url))

    return ret == 0

def get_content(url):
    response = urllib2.urlopen(url)
    content = response.read()
    response.close()
    return content
    