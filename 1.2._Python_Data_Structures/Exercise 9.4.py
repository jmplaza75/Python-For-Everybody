#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 30 17:56:53 2023

@author: josemanuelplaza
"""

name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

count = dict()
for line in handle:
    if not line.startswith("From "):continue
    line = line.split()
    line = line[1]
    count[line] = count.get(line, 0) +1

cc_count = None
word = None
for i,j in count.items():
    if cc_count == None or j > cc_count:
        word = i
        cc_count = j 
print(word, cc_count)