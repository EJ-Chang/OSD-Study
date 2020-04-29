# -*- coding: utf-8 -*-
"""
Created on Tue Apr 7 2020

Written by EJ_Chang
"""

# Function : get inputs from all devices
def getAnything(mouse, joy):
    clicks = mouse.getPressed()
    wheel = list(mouse.getWheelRel())
    dPad = list(joy.getAllHats()[0])
    # dPad = list(joy.getAllHats())
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

    return response_hw, response_key, response_status

# Function : interpret ----
def interpret_key(response_hw, response_key):

    # Setting key map
    if response_hw == 'Mouse':
        if response_key[0] == 1:
            key_meaning = 'Next'
        elif response_key[1] == 1:
            key_meaning = 'OK'
        elif response_key[2] == 1:
            key_meaning = 'Abort'

    elif response_hw == 'Wheel':
        if response_key[1] < 0:
            key_meaning = 'Up'
        elif response_key[1] > 0:
            key_meaning = 'Down'
        elif response_key[0] > 0:
            key_meaning = 'Left'
        elif response_key[0] < 0:
            key_meaning = 'Right'

    elif response_hw == 'dPad':
        if response_key == [0, 1]:
            key_meaning = 'Up'
        elif response_key == [0, -1]:
            key_meaning = 'Down'
        elif response_key == [-1, 0]:
            key_meaning = 'Left'
        elif response_key == [1, 0]:
            key_meaning = 'Right'
        # elif response_key == [1, 1]:
        elif response_key[0] != 0 and response_key[1] != 0:
            key_meaning = 'OK'

    elif response_hw == 'Buttons':
        if response_key[0] == 1:
            key_meaning = 'Abort'

    return key_meaning


# Function : match or not ----
def reponse_checker(response_hw, key_meaning, stimlus_dictionary):

    key_judgement = [0, 0]
    if response_hw == stimlus_dictionary['hardware']:
        key_judgement[0] = 1
    else:
        key_judgement[0] = 0

    if key_meaning == stimlus_dictionary['meaning']:
        key_judgement[1] = 1
    else:
        key_judgement[1] = 0

    final_answer = key_judgement[0] * key_judgement[1]

    return key_judgement, final_answer


# Function : determinant ----
def determine_behavior(key_meaning, item, nTrials, expStatus):
    # if key is in ?
    if key_meaning == 'Abort':
        expStatus = 0

    elif key_meaning == 'Up' or 'Down' or 'Left' or 'Right':
        item += 1
        if item > nTrials - 1:
            item = nTrials - 1
            expStatus = 0

    return item, expStatus

# Function D: trimmer ----

# def trim_off():
