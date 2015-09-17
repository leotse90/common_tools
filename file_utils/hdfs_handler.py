#coding=utf-8
'''
Tools for handle hdfs.

@author: LeoTse
'''

import os


def rmr(file_path):
    # you can use this method remove directory or single file
    return os.system("hadoop dfs -rmr {file_path}".format(file_path=file_path))

def mv(src, dst):
    return os.system("hadoop dfs -mv {src} {dst}".format(src=src, dst=dst))

def ls(path):
    files = []
    if os.system("hadoop dfs -ls {path} > /dev/null".format(path=path)) != 0:
        return files
    lines = os.popen("hadoop dfs -ls {path}".format(path=path)).readlines()
    for i in range(0, len(lines)):
        if lines[i].startswith("Found"):
            continue
        filename = lines[i].replace("\n", "").split(" ")[-1]
        items = filename.split("/")
        items[0] = filename
        files.append(items)
    return files

def exists(file_path):
    return os.system("hadoop dfs -test -e {file_path}".format(file_path=file_path)) == 0

def is_file(path):
    if exists(path):
        files = ls(path)
        return (len(files) == 1 and files[0][0] == path)
    return False

def is_dir(path):
    if exists(path):
        return not is_file(path)
    return False

def put(src, dst):
    return os.system("hadoop dfs -put {src} {dst}".format(src=src, dst=dst))

def get(src, dst):
    return os.system("hadoop dfs -get {src} {dst}".format(src=src, dst=dst))

def read_file(file_path):
    if os.system("hadoop dfs -test -e {file_path}".format(file_path=file_path)) == 0:
        return os.popen('hadoop dfs -cat {file_path}'.format(file_path=file_path)).readlines()
    return None

def read_dir(dir_path):
    if os.system("hadoop dfs -test -e {dir_path}".format(dir_path=dir_path)) == 0:
        return os.popen('hadoop dfs -cat {dir_path}/*'.format(dir_path=dir_path)).readlines()
    return None

def execute_hql(hive_sql):
    return os.system('''hive -e "{hive_sql}"'''.format(hive_sql=hive_sql))
