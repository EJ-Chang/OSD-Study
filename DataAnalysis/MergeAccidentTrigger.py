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

        fields = line.split(" ")
        Direction = fields[1]
        reqRow = int(fields[4])
        reqCol = int(fields[5])
        Answer = int(fields[6])
        ReactionTime = float(fields[8])
        
        if [reqRow, reqCol] == [tarRow, tarCol] :
            # print(line)
            if Direction == 'OK' and Answer == 1:
                pass
            else:
                dataMerge.append([ID, line[:-1], 0])
                # Save lines
                # with open('DelibrateTrigger.txt', 'w') as filehandle: 
                #     for key in dataMerge:
                #         for item in key:
                #             filehandle.writelines('%s ' % item)
                #         filehandle.writelines('\n')
        else:
            tarRow = 6
            tarCol = 6
            pass

        if ReactionTime <= 0.1:
            tarRow = reqRow
            tarCol = reqCol
            # print('Get!')
            # print(line)
            dataMerge.append([ID, line[:-1], reqRow])
            # print('GET:', tarRow, tarCol, ReactionTime)
            # Save lines
            # with open('DelibrateTrigger.txt', 'w') as filehandle: 
            #     for key in dataMerge:
            #         for item in key:
            #             filehandle.writelines('%s ' % item)
            #         filehandle.writelines('\n')

        preRow = reqRow
        preCol = reqCol
#DelibrateTrigger
#AccidentTrigger


with open('AccidentTrigger.txt', 'w') as filehandle: 
    for key in dataMerge:
        for item in key:
            filehandle.writelines('%s ' % item)
        filehandle.writelines('\n')

