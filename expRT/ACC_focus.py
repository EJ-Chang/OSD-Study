# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 2020

Written by EJ_Chang
"""

import os, random, numpy
from psychopy import visual, event, core, monitors
from psychopy.hardware import joystick
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

# Color Palette ----
base03 = (0,43,54)
base0 = (131,148,150)
yellow = (181,137,0)
magenta = (211,54,130)
cyan = (42,161,152)
green = (133,153,0)

# Load initial setting ----
# Preparing Window
my_win = visual.Window(size=(800, 600), pos=(880,1040), 
                       color=base03, colorSpace='rgb255', 
                       monitor = mon, units = 'pix', 
                       screen = 1)

# Preparing Joystick & Mouse
# - Joysticks setting
joystick.backend = 'pyglet'
nJoys = joystick.getNumJoysticks() # Check if I have any joysticks
id = 0 # I'll use the first one as input
joy = joystick.Joystick(id) # ID has to be nJoys - 1
# - Mouse setting
mouse = event.Mouse(visible = True, win = my_win)

# Draw random lines

line_up = visual.ShapeStim(my_win, units = 'pix', lineWidth = 2, 
                          lineColor = yellow, lineColorSpace = 'rgb255', 
                          vertices = ((0, 0), (0, 50)),
                          closeShape = False, pos = (0, 0))
line_up.draw()

line_left = visual.ShapeStim(my_win, units = 'pix', lineWidth = 2, 
                          lineColor = magenta, lineColorSpace = 'rgb255', 
                          vertices = ((-50, 0), (0, 0)),
                          closeShape = False, pos = (0, 0))
line_left.draw()

line_right = visual.ShapeStim(my_win, units = 'pix', lineWidth = 2, 
                          lineColor = cyan, lineColorSpace = 'rgb255', 
                          vertices = ((0, 0), (50, 0)),
                          closeShape = False, pos = (0, 0))
line_right.draw()


line_down = visual.ShapeStim(my_win, units = 'pix', lineWidth = 2, 
                          lineColor = green, lineColorSpace = 'rgb255', 
                          vertices = ((0, 0), (0, -50)),
                          closeShape = False, pos = (0, 0))
line_down.draw()


origin = visual.DotStim(my_win, units = 'pix',
                        # fieldPos = (0,0), fieldSize = (3,3),
                        dotSize=10,
                        color = base0, colorSpace = 'rgb255'
                        )
origin.draw()
# Draw all lines & flip
my_win.flip()
core.wait(2)

# Draw continuous lines

ORIGIN_POINT = (-350, 0) # Y axis = 0
END_POINT = (-250, 50) # Y axis = 0

arrow_up = numpy.array([-10,10])
arrow_down = numpy.array([-10,-10])

line_up = numpy.array([0,50])
line_down = numpy.array([0,-50])
line_right = numpy.array([50,0])
line_left = numpy.array([-50,0])

posList = [(-350,0), (-300,0), (-300,50)]
pos2List = [(-300,0), (-300,50), (-250, 50)]


origin = visual.DotStim(my_win, units = 'pix',
                        fieldPos = ORIGIN_POINT, fieldSize = (3,3),
                        dotSize=10,
                        color = base0, colorSpace = 'rgb255'
                        )
origin.draw()

end = visual.ShapeStim(my_win, units = 'pix', lineWidth = 2, 
                          lineColor = green, lineColorSpace = 'rgb255', 
                          vertices = (END_POINT+arrow_down, 
                                      END_POINT, 
                                      END_POINT+arrow_up),
                          closeShape = False, pos = (0, 0))
end.draw()

current_point = ORIGIN_POINT + line_left

for item in range(3):
    line_next = visual.ShapeStim(my_win, units = 'pix', lineWidth = 2, 
                          lineColor = green, lineColorSpace = 'rgb255', 
                          vertices = (posList[item], pos2List[item]),
                          closeShape = False, pos = (0, 0))
    line_next.draw()
    print(item)

# disk = visual.Circle(my_win, radius = 30, fillColor = 'black', lineColor = None)
# disk.draw()
my_win.flip()
core.wait(2)

# Close window
my_win.close()


