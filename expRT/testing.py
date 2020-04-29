# -*- coding: utf-8 -*-

import math, numpy, random 

from psychopy import core, event, visual, gui, monitors



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

# Preparing Window ----
mywin = visual.Window(size=(1000, 1000), pos=(880,1040), 
                       # color=(0,43,54), colorSpace='rgb255', 
                       monitor = mon, units="pix", 
                       screen = 1)

myClock = core.Clock() 

#create a window
# mywin = visual.Window([800,600],monitor="testMonitor", units="deg")

#create some stimuli
# grating = visual.GratingStim(win=mywin, mask='circle', size=3, pos=[-4,0], sf=3)
fixation = visual.GratingStim(win=mywin, size=0.2, 
                              color = (0,43,54), colorSpace = 'rgb255',
                              pos=[0,0], sf=0)

# Play ground
origin = visual.DotStim(mywin, 
                        units = 'pix',
                        fieldPos = (20,20), 
                        dotSize=10,
                        color = 'red'
                        )

disk = visual.Circle(mywin, radius = 5, 
                     fillColor = 'black', lineColor = 'black',
                     interpolate = True)
square = visual.Rect(mywin, width = 200, height = 200,
 fillColor = 'white',lineColor = None)

#draw the stimuli and update the window
while True: #this creates a never-ending loop
    # grating.setPhase(0.05, '+')#advance phase by 0.05 of a cycle
    # grating.draw()
    disk.draw()
    origin.draw()
    # square.draw()
    mywin.flip()

    if len(event.getKeys())>0:
        break
    event.clearEvents()

#cleanup
mywin.close()
core.quit()