#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# enter two folder paths a and b, and copy files in a to b,
# count the number of copied files. igonore the duplicate 

import sys
import os
import shutil

def copyFiles(src, dst):
    srcFiles = os.listdir(src)
    dstFiles = dict(map(lambda x:[x, ''], os.listdir(dst)))
    filesCopiedNum = 0
    
    for file in srcFiles:
        src_path = os.path.join(src, file)
        dst_path = os.path.join(dst, file)
        # copy the folder. if exist, recursive call this function,
        # otherwise create a new folder then call this function
        if os.path.isdir(src_path):
            if not os.path.isdir(dst_path):
                os.makedirs(dst_path)  
            filesCopiedNum += copyFiles(src_path, dst_path)
        # copy the file. if exist, do nothing
        elif os.path.isfile(src_path):                
            if not dstFiles.has_key(file):
                shutil.copyfile(src_path, dst_path)
                filesCopiedNum += 1
            
    return filesCopiedNum

def test():
    src_dir = os.path.abspath(raw_input('Please enter the source path: '))
    if not os.path.isdir(src_dir):
        print 'Error: source folder does not exist!'
        return 0
    
    dst_dir = os.path.abspath(raw_input('Please enter the destination path: '))
    if os.path.isdir(dst_dir):
        num = copyFiles(src_dir, dst_dir)
    else:
        print 'Destination folder does not exist, a new one will be created.'
        os.makedirs(dst_dir)
        num = copyFiles(src_dir, dst_dir)

    print 'Copy complete:', num, 'files copied.'

if __name__ == '__main__':
    if len(sys.argv) > 1:
        copyFiles(sys.argv[1], sys.argv[2])
    else:
        test()
