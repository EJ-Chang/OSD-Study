# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 2020

Written by EJ_Chang
"""

import os
from os import listdir
from os.path import isfile, join

fileMapping = {
    'RT' : {
        'Directory' : '/Users/YJC/Dropbox/ExpRecord_RT',
        'MergeName' : 'RT_Merge.txt'
        },
    'ACC' : {
        'Directory' : '/Users/YJC/Dropbox/ExpRecord_ACC',
        'MergeName' : 'ACC_Merge.txt'
        },
    'OSD' : {
        'Directory' : '/Users/YJC/Dropbox/ExpRecord_OSD',
        'MergeName' : 'OSD_Merge.txt'
        },
    'BTS' : {
        'Directory' : '/Users/YJC/Dropbox/ExpRecord_BTS',
        'MergeName' : 'BTS_Merge.txt'
        }
}


# Subject profile

whichExp = input("Which experiment data do you want to merge? ").upper()
print('OK, experiment %s is processing...' % whichExp)

# Go to the choosen directory 
os.chdir(fileMapping[whichExp]['Directory'])
# Get file list
fileList = os.listdir(fileMapping[whichExp]['Directory'])

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
    print(ID)
    dataSet = f.readlines()

    # Merge them
    for line in dataSet:
        dataMerge.append([ID,line[:-1]])
        # Save lines
        with open(fileMapping[whichExp]['MergeName'], 'w') as filehandle: 
            for key in dataMerge:
                for item in key:
                    filehandle.writelines('%s ' % item)
                filehandle.writelines('\n')

