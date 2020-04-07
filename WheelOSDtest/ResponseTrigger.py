# -*- coding: utf-8 -*-
"""
Created on Tue Apr 7 2020

Written by EJ_Chang
"""

# Def block START ====
def response_key(userInput, inputTime, stimuli, nStimulus, expStatus):
    # global expStatus, item
    x = stimuli
    if userInput[2] == 1:
        expStatus = 0
    elif userInput[0] == 1:
        x = stimuli + 1
        if x > nStimulus - 1:
            x = nStimulus - 1
    item = stimuli
    return x, expStatus
# Def block END ====