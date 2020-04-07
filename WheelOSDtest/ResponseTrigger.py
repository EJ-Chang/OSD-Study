# -*- coding: utf-8 -*-
"""
Created on Tue Apr 7 2020

Written by EJ_Chang
"""

# Def block START ====
def response_key(userInput, inputTime, stimuli, nStimulus):
    global expStatus, item
    expStatus
    if userInput[2] == 1:
        print(inputTime)
        expStatus = 0
        # return expStatus
        # break
    elif userInput[0] == 1:
        stimuli = stimuli + 1
        if stimuli > nStimulus - 1:
            stimuli = nStimulus - 1
            item = stimuli
            print(item)
        print('Next stimuli.') # TODO: set key blocking

    # return item
# Def block END ====