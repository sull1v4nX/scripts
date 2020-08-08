#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Version: 1
Created on Wed Jul  1 18:38:55 2020

@author: Sull1v4nX 
"""

import difflib
file1 = open('original.txt', 'r').readlines()
file2 = open('site2.txt','r').readlines()

htmlDiffer = difflib.HtmlDiff()
htmldiffs = htmlDiffer.make_file(file1, file2)

with open('comparison.html', 'w') as outfile:
    outfile.write(htmldiffs)
    
print("Fin del programa")

