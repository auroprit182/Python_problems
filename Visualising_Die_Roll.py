#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 20:29:33 2020

@author: auropritbhanjadeo

Visualising Die Roll Frequencies and Percentages
Graphing frequencies of die rolls with Seaborn.

"""

import matplotlib.pyplot as plt
import numpy as np
import random
import seaborn as sns
import sys


# use list comprehension to create a list of rolls of a six-sided die

#rolls = [random.randrange(1, 7) for i in range(int(sys.argv[1]))] #use this for script
rolls = [random.randrange(1, 7) for i in range(int(input('Enter number of rolls: ')))]

# NumPy unique function returns unique faces and frequency of each face
values , Frequencies = np.unique(rolls,return_counts=True)

title = f'Rolling a Six-Sided Die {len(rolls):,} Times'
sns.set_style('whitegrid')

axes=sns.barplot(x=values,y=Frequencies,palette='bright')
axes.set_title(title)
axes.set(xlabel='Die Value',ylabel='Frequency')
# scale y-axis by 10% to make room for text above bars
axes.set_ylim(top=max(Frequencies)*1.10)

# display frequency & percentage above each patch (bar)
for bar,frequency in zip(axes.patches,Frequencies):
    text_x = bar.get_x() + bar.get_width()/2.0
    text_y = bar.get_height()
    text=f'{frequency:,}\n{frequency/len(rolls):.3%}'
    axes.text(text_x,text_y,text,fontsize=11,ha='center',va='bottom')
    
plt.show()   #display graph