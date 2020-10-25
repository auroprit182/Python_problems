#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 24 17:09:01 2020

@author: auropritbhanjadeo
Tokenizing a string and counting unique words

"""

text = ('this is sample text with several words '
        'this is more sample text with some differen words')

word_counts = {}

#count occurence of each word

for words in text.split():
    if words in word_counts:
        word_counts[words]+=1 #update existing key value pair
    else:
        word_counts[words]=1 #add new key value pair
        
print(f'{"WORD":<12}COUNT')

for word,counts in sorted(word_counts.items()):
    print(f'{word:<12}{counts}')
      
print('\nNumber of unique words:',len(word_counts))
        
        

