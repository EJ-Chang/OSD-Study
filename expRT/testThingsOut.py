# -*- coding: utf-8 -*-

import os, random
import numpy as np

dir_DictList= []
with open("dir_limit.txt") as f:
    for line in f:
        (number, main_dir, ortho_dir_1, ortho_dir_2) = line.split()
        sti_Dict = {
        'number': number,
        'main_dir': main_dir,
        'ortho_dir': [ortho_dir_1,ortho_dir_2]
        }
        dir_DictList.append(sti_Dict)
        print(sti_Dict)

print(type(dir_DictList))

# # Draw crosshair with a center dot
# line_up = visual.ShapeStim(my_win, units = 'pix', lineWidth = 2, 
#                           lineColor = yellow, lineColorSpace = 'rgb255', 
#                           vertices = ((0, 0), (0, 50)),
#                           closeShape = False, pos = (0, 0))
# line_up.draw()

# line_left = visual.ShapeStim(my_win, units = 'pix', lineWidth = 2, 
#                           lineColor = magenta, lineColorSpace = 'rgb255', 
#                           vertices = ((-50, 0), (0, 0)),
#                           closeShape = False, pos = (0, 0))
# line_left.draw()

# line_right = visual.ShapeStim(my_win, units = 'pix', lineWidth = 2, 
#                           lineColor = cyan, lineColorSpace = 'rgb255', 
#                           vertices = ((0, 0), (50, 0)),
#                           closeShape = False, pos = (0, 0))
# line_right.draw()


# line_down = visual.ShapeStim(my_win, units = 'pix', lineWidth = 2, 
#                           lineColor = green, lineColorSpace = 'rgb255', 
#                           vertices = ((0, 0), (0, -50)),
#                           closeShape = False, pos = (0, 0))
# line_down.draw()

# origin = visual.DotStim(my_win, units = 'pix',
#                         # fieldPos = (0,0), fieldSize = (3,3),
#                         dotSize=10,
#                         color = base0, colorSpace = 'rgb255'
#                         )
# origin.draw()
# my_win.flip()
# core.wait(2)