# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 2020

Written by EJ_Chang
"""

import os
from os import listdir
from os.path import isfile, join


# Go to the choosen directory 
os.chdir('/Users/YJC/Dropbox/ExpRecord_OSD')
# Get file list
fileList = os.listdir('/Users/YJC/Dropbox/ExpRecord_OSD')

dataFiles = []
for files in fileList:
    if (files.endswith('.txt') and files.startswith('2020')):
        dataFiles.append(files)

# Initial value
dataMerge = []
ID = 0

# Read files from the list, adding ID to is
for data in dataFiles:
    f = open(data, 'r')
    ID += 1
    # print(ID)
    dataSet = f.readlines()
    tarRow = 6
    tarCol = 6
    preRow = 0
    preCol = 0
    # Merge them
    for line in dataSet:

        if 'NoMeaning' in line:
            pass
        else:

            fields = line.split(" ")
            Direction = fields[1]
            reqRow = int(fields[4])
            reqCol = int(fields[5])
            Answer = int(fields[6])
            ReactionTime = float(fields[8])

            if ReactionTime <= 0.1:
                tarRow = reqRow
                tarCol = reqCol

            if [reqRow, reqCol] == [tarRow, tarCol] :
                dataMerge.append([ID, line[:-1], 0])
            else:
                tarRow = 6
                tarCol = 6
                dataMerge.append([ID, line[:-1], 1])

            preRow = reqRow
            preCol = reqCol
#DelibrateTrigger
#AccidentTrigger


with open('DelibrateTrigger.txt', 'w') as filehandle: 
    for key in dataMerge:
        for item in key:
            filehandle.writelines('%s ' % item)
        filehandle.writelines('\n')

