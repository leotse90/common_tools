#coding=utf-8
'''
Dictionary related operations.

@author: LeoTse
'''

def order_by_value(src_dict, reverse=False):
    '''
        Sort a dictionary by value and return a tuple.
        For example:
        Input: {"a":3, "c":1, "b":4}
        Output: [('c', 1), ('a', 3), ('b', 4)]
    '''
    return sorted(src_dict.items(), key=lambda d:d[1], reverse=reverse)
    
def order_by_key(src_dict, reverse=False):
    '''
        Sort a dictionary by key and return a tuple.
        For example:
        Input: {"a":3, "c":1, "b":4}
        Output: [('a', 3), ('b', 4), ('c', 1)]
    '''
    return [(key, src_dict[key]) for key in sorted(src_dict.keys(), reverse=reverse)]

def merge_two_dicts(dict1, dict2):
    '''
        Merge two dictionaries into a dictionary and return.
        If more than one dictionary have the same key, the last value will appear in the result.
    '''
    return merge_dicts([dict1, dict2])

def merge_dicts(dict_list):
    '''
        Merge a list of dictionaries into a dictionary and return.
        If more than one dictionary have the same key, the last value will appear in the result.
    '''
    result = {}
    for tmp_dict in dict_list:
        result.update(tmp_dict)
    return result

if __name__ == "__main__":
    test_dict = {"a":3, "c":1, "b":4}
    print order_by_value(test_dict, reverse=False)
    print order_by_key(test_dict, reverse=False)
    
    dict1 = {"a":1, "b":2}
    dict2 = {"a":2}
    dict3 = {"a":3, "c":5}
    print merge_dicts([dict1, dict2, dict3])
    print merge_two_dicts(dict1, dict2)
    
