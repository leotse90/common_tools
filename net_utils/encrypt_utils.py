#coding=utf-8

'''
encrypt steps:
1.base64 encrypt -> str1;
2.APPENDIX + str1 -> str2;
3.base64 encrypt str2 -> str3;
4.str3 + str2[-RANDOM_NUMS_COUNT:] -> str4
5.case conversion at every location -> encrypt result;

@author:leotse
'''

import base64

PREFIX = u'leotse'
RANDOM_NUMS_COUNT = 3

def lt_encrypt(source):
    bstr1 = base64.b64encode(source)
    bstr1 = PREFIX + bstr1
    random_appendix = bstr1[-RANDOM_NUMS_COUNT:]
    bstr2 = base64.b64encode(bstr1)
    astr = bstr2 + random_appendix
    encrypt_str = astr.swapcase()
    return encrypt_str

def lt_decrypt(source):
    cstr = source.swapcase()
    astr = cstr[:-RANDOM_NUMS_COUNT]
    dstr1 = base64.b64decode(astr)
    astr = dstr1[len(PREFIX):]
    decrypt_str = base64.b64decode(astr)
    return decrypt_str
