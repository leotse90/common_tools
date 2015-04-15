#coding:utf8

'''
Tools for Http request and response.

@author: LeoTse
'''

import urllib2

def get_content(url):
    response = urllib2.urlopen(url)
    content = response.read()
    response.close()
    return content

if __name__ == "__main__":
    print get_content("http://www.xuetangx.com/")
