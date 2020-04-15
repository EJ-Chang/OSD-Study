# -*- coding: utf-8 -*-
"""
Created on Tue Apr 15 2020

Written by EJ_Chang
"""


lineNumber = 1
imageList=[]
with open("sti_files.txt") as f:
    for line in f:
        (number, hw, mean, filepath) = line.split()
        sti_Dict = {
        'number': lineNumber,
        'hardware': hw,
        'meaning': mean,
        'path': filepath
        }
        lineNumber += 1
        imageList.append(sti_Dict)

# print (sti_Dict)
# print(imageList)
# print(imageList[0])
# print(imageList[0]['path'])
# print(imageList[0]['meaning'])