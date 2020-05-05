# -*- coding: utf-8 -*-

import math, numpy, random
from psychopy.hardware import joystick
from psychopy import core, event, visual, gui, monitors
from ResponseTrigger import *
from datetime import date

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



# Subject profile
today = date.today()
print('Today is %s:' % today)
usernum = int(input('Please enter subject number:'))
username = input("Please enter your name:").upper()
print('Hi %s, welcome to our experiment!' % username)

if usernum % 2 == 1:
    hw_required = ['Wheel','dPad']
elif usernum % 2 == 0:
    hw_required = ['dPad', 'Wheel']

print(hw_required)


# Preparing Window ----
my_win = visual.Window(size=(800, 800), pos=(880,1040), 
                       color=(0,43,54), colorSpace='rgb255', 
                       monitor = mon, units = 'pix', 
                       screen = 1)


# Preparing pics ----
img_start = 'start.png'
img_rest = 'rest.png'
img_ty = 'thanks.png'

instruction_dict = {
    'Wheel': 'acc1.png',
    'dPad':  'acc2.png'}

# pic in screen test
img = visual.ImageStim(win = my_win, image = img_start, 
                       units = 'pix')
img.draw()
my_win.flip()
core.wait(2)

for block in range(2):
    img = visual.ImageStim(win = my_win, image = instruction_dict[hw_required[block]], 
                           units = 'pix')
    img.draw()
    my_win.flip()
    core.wait(2)

    img = visual.ImageStim(win = my_win, image = img_rest, 
                           units = 'pix')
    img.draw()
    my_win.flip()
    core.wait(2)

img = visual.ImageStim(win = my_win, image = img_ty, 
                       units = 'pix')
img.draw()
my_win.flip()
core.wait(2)
