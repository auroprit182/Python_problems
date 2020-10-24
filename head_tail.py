#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 18:57:07 2020

@author: auropritbhanjadeo

Create a random number generator function to display head or tail for 20 coin flips

"""

import random

for flips in range(1,21):
    value  = random.randrange(1,3)
    
    if value == 1:
        disp = 'T'
    else:
        disp = 'H'
        
    print(f'{disp}',end=' ')
    

    
        

