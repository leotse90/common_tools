#coding=utf-8
'''
List related operations.

@author: LeoTse
'''

def insert_list_into_list(index, insert_list, src_list):
    '''
        Insert elements in  insert_list before index into given list then return.
        This function is different from L.insert(index, object), which  insert object before index,
        insert_list_into_list(index, insert_list, src_list) works like merge two list.
        
        For example:
        Input: insert_pos = 1, insert_data = [2, 5], src_list = [1, 3, 4]
        Output: [1, 2, 5, 3, 4]
    '''
    src_list[index:index] = insert_list
    return src_list

if __name__ == "__main__":
    t_list = [1, 4, 5, 6]
    t_list.insert(1, [2, 3])
    print t_list
    
    t_list = [1, 4, 5, 6]
    print insert_list_into_list(1, [2, 3], t_list)
