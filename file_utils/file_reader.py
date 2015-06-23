#coding=utf-8
'''
Tools for read a file or a directory.

@author: LeoTse
'''

import os
import time
import stat
import datetime

def make_sure_dir_exists(dirname):
    # check if a directory exists and create it if not.
    if not os.path.exists(dirname):
        os.makedirs(dirname)
    elif not os.path.isdir(dirname):
        raise Exception("Given path exists and it's not a directory.")
    
def get_all_file_paths(dirname):
    # return the file paths in a directory by walking the tree.
    file_paths = []
    for root, _, files in os.walk(dirname):
        for file_name in files:
            file_paths.append(os.path.join(root, file_name))
            
        # you also can use below to get all files, you should use extend cause
        # the container file_paths initial in every loop. 
#         file_paths.extend([os.path.join(root, file_name) for file_name in files])     

    return file_paths
    
def yield_all_file_paths(dirname):
    # recommend you use this function instead of get_all_file_paths 
    # when there are a lot of files in the directory. 
    for root, _, files in os.walk(dirname):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            yield file_path
    
def get_file_mtime(filepath):
    # get file create time
    # format example: "2015-05-27 14:40:00"
    return datetime.datetime.utcfromtimestamp(time.mktime(time.localtime(os.stat(filepath).st_mtime))).strftime("%Y-%m-%d %H:%M:%S")
    
def remove_file(filepath):
    # remove file by path if exists
    if os.path.exists(filepath) and os.path.isfile(filepath):
        os.remove(filepath)

def remove_dir_tree(dir, include_self = True):
    if dir and os.path.isdir(dir):
        walker = os.walk(dir, False)
        for item in walker:
            for d in item[1]:
                p = os.path.join(item[0], d)
                os.rmdir(p)
            for f in item[2]:
                p = os.path.join(item[0], f)
                os.chmod(p, stat.S_IWUSR)
                os.remove(p)

        if include_self:
            os.rmdir(dir)

    
if __name__ == "__main__":
    dirname = r'C:\Develop\test'
    for filepath in yield_all_file_paths(dirname):
        print filepath
