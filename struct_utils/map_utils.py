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



if __name__ == "__main__":
    test_dict = {"a":3, "c":1, "b":4}
    print order_by_value(test_dict, reverse=False)
    print order_by_key(test_dict, reverse=False)
