#coding=utf-8
'''
Tools for read a file or a directory.

@author: LeoTse
'''

import os

def make_sure_dir_exists(dirname):
    '''
        Check if a directory exists and create it if not.
    '''
    if not os.path.exists(dirname):
        os.makedirs(dirname)
    elif not os.path.isdir(dirname):
        raise Exception("Given path exists and it's not a directory.")
    
def get_all_file_paths(dirname):
    '''
        Return the file paths in a directory by walking the tree.
    '''
    file_paths = []
    for root, _, files in os.walk(dirname):
        for file_name in files:
            file_paths.append(os.path.join(root, file_name))
    return file_paths
    
if __name__ == "__main__":
    dirname = r'C:\Develop\test'
    print get_all_file_paths(dirname)
