#coding=utf-8
'''
Tools for parse given line in a file.

@author: LeoTse
'''

import re
import json

PATTERN_JSON = re.compile(r'^.*?(\{.*\})\s*$')

def extract_dict_from_line(line, nested=False):
    '''
        Return a dict from given line exists, or return None.
    '''
    try:
        parsed_dict = json.loads(line)
    except Exception:
        if not nested:
            json_match = PATTERN_JSON.match(line)
            if json_match:
                return extract_dict_from_line(json_match.group(1), nested=True)
        return None
    return parsed_dict

if __name__ == "__main__":
    line_info = 'This is a test line:{"name":"leo", "age":24}'
    print type(extract_dict_from_line(line_info))