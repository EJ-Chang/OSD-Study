# -*- coding: utf-8 -*-
"""
Created on Tue Apr 7 2020

Written by EJ_Chang
"""

# Def block START ====
def response_key(userInput, inputTime, stimuli, nStimulus, expStatus):
    # global expStatus, item
    item = stimuli
    if userInput[2] == 1:
        expStatus = 0
    elif userInput[0] == 1:
        item = stimuli + 1
        if item > nStimulus - 1:
            item = nStimulus - 1
    return item, expStatus # Export 2 variables
# Def block END ====