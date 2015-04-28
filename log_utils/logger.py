#coding=utf-8

'''
    Tools for write log, and split logs into small partitions.
    (Modified by LeoTse)
    @author: LeoTse
'''

import os
import sys
import logging

from logging.handlers import MemoryHandler, RotatingFileHandler

from file_utils.file_reader import make_sure_dir_exists

# log save path
LOG_PATH = "/tmp/logs"

class Logger:

    '''
        Init Logger object.
        
        @param size: size of partitions(MB)
        @param backupCount: the maximum number of backup logs
        @param cacheRecords: log content flush to disk when log numbers in cache 
                            reach this(except level beyond flushLevel)   
    '''
    def __init__(self, name, size = 10, backupCount = 50, cacheRecords = 1, print_to_console=True): 
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.DEBUG)
        
        logdir = os.path.join(LOG_PATH, name)
        make_sure_dir_exists(logdir)
        logfile = os.path.join(logdir, '%s.log' % name)
        
        hdlr = RotatingFileHandler(logfile, 'a', maxBytes=1024 * 1024 *size, backupCount=backupCount)
        hdlr.setFormatter(logging.Formatter('%(asctime)s %(message)s'))
        mh = MemoryHandler(cacheRecords,flushLevel=logging.INFO, target=hdlr)
        self.logger.addHandler(mh)
        if print_to_console:
            hdlr = logging.StreamHandler(sys.stdout)
            hdlr.setFormatter(logging.Formatter("%(message)s", ""))
            hdlr.setLevel(logging.DEBUG)
            self.logger.addHandler(hdlr)

    def getLogger(self):
        return self.logger
