#coding=utf-8

'''
encrypt steps:
1.append APPENDIX to string -> str1;
2.base64 encrypt -> str2;
3.base64 encrypt -> str3;
4.str3 + str2[-RANDOM_NUMS_COUNT:] -> str4
5.case conversion at every location -> encrypt result;

@author:leotse
'''

import random
import base64

APPENDIX = u'leotse'
RANDOM_NUMS_COUNT = 3

def lt_encrypt(source):
	source += APPENDIX
	bstr1 = base64.b64encode(source)
	random_appendix = bstr1[-RANDOM_NUMS_COUNT:]
	bstr2 = base64.b64encode(bstr1)
	astr = bstr2 + random_appendix
	encrypt_str = case_convert(astr)
	return encrypt_str

def lt_decrypt(source):
	cstr = case_convert(source)
	astr = cstr[:-RANDOM_NUMS_COUNT]
	dstr1 = base64.b64decode(astr)
	dstr2 = base64.b64decode(dstr1)
	decrypt_str = dstr2[:-len(APPENDIX)]
	return decrypt_str

def case_convert(str):
	n_str = u""
	for c in str:
		if c.isupper():
			n_str += c.lower()
		else:
			n_str += c.upper()

	return n_str

