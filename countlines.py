#!/usr/bin/env python

'countlines.py -- count the lines of files end by ".*" in a folder.'

import os

def countLines(filename):
    count = 0
    f = open(filename, 'r')
    for eachline in f:
        count += 1
    f.close()
    return count

def getFilePathsDict(path):
    pyDict = {}
    filesList = os.listdir(path)
    for each in filesList:
        filepath = os.path.join(path, each)
        if os.path.isfile(filepath) and (each.endswith('.h') or each.endswith('.cpp') or each.endswith('.cu')):  # change this line to choose the file kinds you want to count
            pyDict[filepath] = 0
        elif os.path.isdir(filepath):
            pyDict = dict(pyDict, **getFilePathsDict(filepath))   # recursive when it is a folder
    return pyDict

def getTotalNumber(pyDict):
    return sum(pyDict.values())

def showEachFileNumber(pyDict):
    print 'File Name\t\tLine Number'
    print '-' * 40
    for key in sorted(pyDict):
        print '%s\t%s' % (os.path.basename(key).ljust(20), pyDict[key])

def main():
    path = raw_input('Please enter the folder path: ').strip()			# 输入需要统计的文件夹路径
    pyDict = getFilePathsDict(path)
    for key in pyDict:
        pyDict[key] = countLines(key)
    sum = getTotalNumber(pyDict)
    print 'The total line number is %d.' % sum
    print 'Details:'
    showEachFileNumber(pyDict)

if __name__ == '__main__':
    main()

