# -*- coding: utf-8 -*-


import os
from os import listdir
from os.path import isfile, join

# Initial value
dataMerge = []
ID = 0

# open file
f = open('/Users/YJC/Dropbox/UsabilityTesting/DataAnalysis/testDATA.txt', 'r')
dataSet = f.readlines()

# Merge them
for line in dataSet:
    if 'NoMeaning' in line:
        pass
    else:
        print(line[:-1])
        dataMerge.append([ID, line[:-1]])
        with open('testMerge.txt', 'w') as filehandle: 
            for key in dataMerge:
                for item in key:
                    filehandle.writelines('%s ' % item)
                filehandle.writelines('\n')


print('end')

