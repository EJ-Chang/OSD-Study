# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 2020

Written by EJ_Chang
"""
import os, random
# Function A: Generate line directions

def dirGenerate(dir_DictList):

    # Main directions
    main_que = []
    main_que_num = []
    ortho_que = []
    sub_que = []
    for i in range(1):
        seed = random.randrange(4)
        main = dir_DictList[seed]['main_dir']
        orthogonal = dir_DictList[seed]['ortho_dir']

        # Derivation directions (up to 3 choices)
        pre_que = main[:]
        sub_que.append(pre_que)
        que_pool = orthogonal[:] # Copy orthogonal. Avoid changning orthogonal
        que_pool += [main]

        for k in range(9):

            sequal = random.choice(que_pool)
            sub_que.append(sequal)

            if sequal in orthogonal:
                que_pool = [sequal, main]
            else:
                que_pool = orthogonal[:] # Copy orthogonal. Avoid changning orthogonal
                que_pool += [main]

            pre_que = sequal[:]
    return sub_que