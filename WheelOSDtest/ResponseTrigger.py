# -*- coding: utf-8 -*-
"""
Created on Tue Apr 7 2020

Written by EJ_Chang
"""

# Function A+B ==== Current solution
def response_key(userInput, inputTime, stimuli, nStimulus, expStatus):
    # global expStatus, item
    item = stimuli
    if userInput[2] == 1:
        expStatus = 0
    elif userInput[0] == 1:
        item = stimuli + 1
        if item > nStimulus - 1:
            item = nStimulus - 1 # Turn to ending page
    return item, expStatus # Export 2 variables

# Building =================================
# Function A: interpret ----
def interpret_key():
    if sum(userInput) >= 1: # Check at least one key was pressed
        # Get Pressed
        if userInput[0] == 1:
            userResponse = 'next'
        elif userInput[1] == 1:
            userResponse = 'next'
        elif userInput[2] == 1:
            userResponse = 'Exit'
            expStatus = 0

        # Get Wheel
        if (x,y) == (0,1):
            userResponse = 'up'
        elif (x,y) == (0, -1):
            userResponse = 'down'
        elif (x,y) == (1,0):
            userResponse = 'left'
        elif (x,y) ==(-1,0):
            userResponse = 'right'

        # Get Joystick Dpad
        if dPad == [(0, 1)]:
            userResponse = 'up'
        elif dPad == [(0, -1)]:
            userResponse = 'down'
        elif dPad == [(1, 0)]:
            userResponse = 'left'
        elif dPad == [(-1, 0)] or dPad == [(1,1)]:
            userResponse = 'right'

# Function B: determinant ----

# def determinant_feedback():

# Function C: trimmer ----

# def trim_off():


# Function 0: getAnything ----
# def getAnything():