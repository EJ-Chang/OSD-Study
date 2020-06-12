# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 2020

Written by EJ_Chang
"""

import os, random
from psychopy import visual, event, core, monitors
from psychopy.hardware import joystick
from datetime import date
from ResponseTrigger import *

# Subject profile
today = date.today()
print('Today is %s:' % today)
username = input("Please enter your name:").upper()
print('Hi %s, welcome to our experiment!' % username)

# Make screen profile ----
widthPix = 2560 # screen width in px
heightPix = 1440 # screen height in px
monitorwidth = 60 # monitor width in cm
viewdist = 60 # viewing distance in cm
monitorname = 'ProArt27'
scrn = 0 # 0 to use main screen, 1 to use external screen
mon = monitors.Monitor(monitorname, width=monitorwidth, distance=viewdist)
mon.setSizePix((widthPix, heightPix))
mon.save()


# Load initial setting ----
# Preparing Window
# my_win = visual.Window(size=(800, 600), pos=(880,1040), monitor = mon, units = 'pix', 
#                        screen = 1)
my_win = visual.Window(size=(2560, 1440), pos=(0,0), monitor = mon, units = 'pix', 
                       screen = 0, fullscr = 1)


# Preparing Joystick & Mouse
# - Joysticks setting
joystick.backend = 'pyglet'
nJoys = joystick.getNumJoysticks() # Check if I have any joysticks
id = 0 # I'll use the first one as input
joy = joystick.Joystick(id) # ID has to be nJoys - 1
# - Mouse setting
mouse = event.Mouse(visible = True, win = my_win)
mouse.clickReset() # Reset to its initials

# Preparing experiment stimulus
img_start = 'OSD_ImgFolder/start.png'
img_rest = 'OSD_ImgFolder/rest.png'
img_ty = 'OSD_ImgFolder/thanks.png'
lineNumber = 1
imageLUT = [] # list of image dictionary
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
        imageLUT.append(sti_Dict)

# Randomizing the list
nStimulus = len(imageLUT)  # nStimulus = 10
playList = list(range(nStimulus)) * 10 # playList = [0,1,2,...nStimulus] repeats twice
nTrials = len(playList)
random.shuffle(playList) # Shuffle the playList
stimulus_seq = tuple(playList) # Make it unchangable

# Preparing experiment timer
experiment_timer = core.Clock()
experiment_timer.reset()

# Setting initial numbers
item = 0
pre_key = []
expStatus = 1
response = []


# Start experiment ----
# Greeting page
img = visual.ImageStim(win = my_win, image = img_start, 
                       units = 'pix')
img.draw()
my_win.flip()
core.wait(2)

stimuli_time =core.getTime()

# Trials
while expStatus == 1:

    img = visual.ImageStim(win = my_win, 
                           image = imageLUT[stimulus_seq[item]]['path'],
                           units = 'pix')
    img.draw()
    my_win.flip()

    # Get response
    response_hw, response_key, response_status = getAnything(mouse, joy)
    
    # if clicks != pre_mouse and response_status == 1:
    if response_status == 1 and response_key != pre_key:

        current_time = core.getTime()

        if current_time - stimuli_time > 0.3: # RT minimum

            key_meaning = interpret_key(response_hw, response_key) 

            key_judgement, final_answer = reponse_checker(response_hw, 
                                                          key_meaning, 
                                                          imageLUT[stimulus_seq[item]])

            item, expStatus = determine_behavior(key_meaning, item,
             nTrials, expStatus)


            # Determine response key & time
            response.append([stimulus_seq[item-1], 
                            response_hw, 
                            key_meaning,
                            imageLUT[stimulus_seq[item]]['hardware'],
                            imageLUT[stimulus_seq[item]]['meaning'],
                            final_answer,
                            current_time -  stimuli_time,
                            current_time
                            ]) # correct/not, RT, real time

            # Resting time between stimulus
            img = visual.ImageStim(win = my_win, image = img_rest, 
                               units = 'pix')
            img.draw()
            my_win.flip()

            # Stimulus interval
            t = 0.3 + random.randrange(2)
            core.wait(t)
            # print(t)
            stimuli_time = core.getTime()


    pre_key = response_key # Button status update

# Thank u page
img = visual.ImageStim(win = my_win, image = img_ty, units = 'pix')
img.draw()
my_win.flip()
core.wait(2)

# Close window
my_win.close()


# Exp END ----
# print('Get your responses:', response)

# Experiment record file
os.chdir('/Users/YJC/Dropbox/ExpRecord_RT')
filename = ('%s_%s.txt' % (today, username))
filecount = 0

while os.path.isfile(filename):
    filecount += 1
    filename = ('%s_%s_%d.txt' % (today, username, filecount))


with open(filename, 'w') as filehandle: 
    for key in response:
        for item in key:
            filehandle.writelines("%s " % item)
        filehandle.writelines("\n")
