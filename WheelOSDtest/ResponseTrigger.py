# -*- coding: utf-8 -*-
"""
Created on Tue Apr 7 2020

Written by EJ_Chang
"""

# Function 0 ===== get inputs from all devices
def getAnything(mouse, joy):
    clicks = mouse.getPressed()
    wheel = list(mouse.getWheelRel())
    dPad = list(joy.getAllHats()[0])
    but_x = int(joy.getButton(0))
    buttons = [but_x] # Can be modified to collect more buttons

    if clicks != [0, 0, 0]:
        response_status = 1
        response_hw = 'mouse'
        response_key = clicks
    elif wheel != [0, 0]:
        response_status = 1
        response_hw = 'wheel'
        response_key = wheel
    elif dPad != [0, 0]:
        response_status = 1
        response_hw = 'dpad'
        response_key = dPad
    elif buttons != [0]:
        response_status = 1
        response_hw = 'buttons'
        response_key = buttons
    else:
        response_status = 0
        response_hw = 'none'
        response_key = []

    # return clicks, wheel, dPad, buttons, response_status, response_hw
    return response_hw, response_key, response_status

# Function A+B ==== Current solution
def response_key(userInput, stimuli, nStimulus, expStatus):
    # global expStatus, item
    item = stimuli
    if userInput[2] == 1:
        expStatus = 0
    elif userInput[0] == 1:
        item = stimuli + 1
        if item > nStimulus - 1:
            item = nStimulus - 1
            expStatus = 0
    return item, expStatus # Export 2 variables

# Building =================================
# Function A: interpret ----
def interpret_key(response_hw, response_key, stimuli, nStimulus, expStatus):
    item = stimuli

    if response_hw == 'mouse':
        if response_key[0] == 1:
            item = stimuli + 1 
            if item > nStimulus - 1:
                item = nStimulus - 1
                expStatus = 0
        elif response_key[2] == 1:
            expStatus = 0
    elif response_hw == 'dpad':
        if response_key == [0, -1]:
            item = stimuli + 1
            if item > nStimulus - 1:
                item = nStimulus - 1
                expStatus = 0
    elif response_hw == 'buttons':
        if response_key[0] == 1:
            expStatus = 0

    return item, expStatus




# Function B: determinant ----

# def determinant_feedback():

# Function C: trimmer ----

# def trim_off():


# Function 0: getAnything ----
# def getAnything():