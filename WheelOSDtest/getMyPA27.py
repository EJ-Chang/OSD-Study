

from psychopy import visual, event, core, monitors
from psychopy.hardware import joystick

SCREENWIDTH = int(2560)
SCREENHEIGHT = int(1440)

mon = monitors.Monitor("default", width=monitorwidth, distance=viewdist)
print(mon)