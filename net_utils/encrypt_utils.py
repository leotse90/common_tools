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

import random
import base64

APPENDIX = u'leotse'
RANDOM_NUMS_COUNT = 3

def lt_encrypt(source):
	bstr1 = base64.b64encode(source)
	bstr1 = APPENDIX + bstr1
	random_appendix = bstr1[-RANDOM_NUMS_COUNT:]
	bstr2 = base64.b64encode(bstr1)
	astr = bstr2 + random_appendix
	encrypt_str = case_convert(astr)
	return encrypt_str

def lt_decrypt(source):
	cstr = case_convert(source)
	astr = cstr[:-RANDOM_NUMS_COUNT]
	dstr1 = base64.b64decode(astr)
	astr = dstr1[len(APPENDIX):]
	decrypt_str = base64.b64decode(astr)
	return decrypt_str

def case_convert(str):
	n_str = u""
	for c in str:
		if c.isupper():
			n_str += c.lower()
		else:
			n_str += c.upper()

	return n_str

