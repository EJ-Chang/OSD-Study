# -*- coding: utf-8 -*-
"""
Created on Thu Jan 2 2020

Special thanks to: u0118077
Modified by EJ_Chang on Jan 6 2020
"""


import psychopy.visual
import psychopy.core
import psychopy.hardware.joystick
import pyglet

joysticks = pyglet.input.get_joysticks()

if joysticks:
    joystick = joysticks[0]
joystick.open()

print(joystick)