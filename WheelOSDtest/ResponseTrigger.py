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
        response_hw = 'Mouse'
        response_key = clicks
    elif wheel != [0, 0]:
        response_status = 1
        response_hw = 'Wheel'
        response_key = wheel
    elif dPad != [0, 0]:
        response_status = 1
        response_hw = 'dPad'
        response_key = dPad
    elif buttons != [0]:
        response_status = 1
        response_hw = 'Buttons'
        response_key = buttons
    else:
        response_status = 0
        response_hw = 'None'
        response_key = []

    # return clicks, wheel, dPad, buttons, response_status, response_hw
    return response_hw, response_key, response_status

# Function A+B ==== Current solution
def response_key(userInput, item, nStimulus, expStatus):

    if userInput[2] == 1:
        expStatus = 0
    elif userInput[0] == 1:
        item += 1
        if item > nStimulus - 1:
            item -= 1
            expStatus = 0
    return item, expStatus # Export 2 variables

# Building =================================
# Function A: interpret ----
def interpret_key(response_hw, response_key):

    if response_hw == 'Mouse':
        if response_key[0] == 1:
            key_meaning = 'Next'
        elif response_key[2] == 1:
            key_meaning = 'Abort'
        else:
            key_meaning = 'None'

    elif response_hw == 'Wheel':
        if response_key[1] > 0:
            key_meaning = 'Next'
        elif response_key[1] < 0:
            key_meaning = 'Previous'
        else:
            key_meaning = 'None'

    elif response_hw == 'dPad':
        if response_key == [0, -1]:
            key_meaning = 'Next'
        elif response_key == [0, 1]:
            key_meaning = 'Previous'
        else:
            key_meaning = 'None'

    elif response_hw == 'Buttons':
        if response_key[0] == 1:
            key_meaning = 'Abort'

    elif response_hw == 'None':
        key_meaning = 'None'

    else:
        key_meaning = 'None'

    return key_meaning

# Function B: determinant ----
def determine_behavior(key_meaning, item, nStimulus, expStatus):

    if key_meaning == 'Next':
        item += 1
        if item > nStimulus - 1:
            item = nStimulus - 1
            expStatus = 0
    elif key_meaning == 'Previous':
        item -= 1
        if item < 0:
            item = 0
    elif key_meaning == 'Abort':
        expStatus = 0

    return item, expStatus





# def determinant_feedback():

# Function C: trimmer ----

# def trim_off():


# Function 0: getAnything ----
# def getAnything():