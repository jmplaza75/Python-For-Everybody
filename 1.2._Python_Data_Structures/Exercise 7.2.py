#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 29 10:42:56 2023

@author: josemanuelplaza
"""

# Use the file name mbox-short.txt as the file name
tot=0
counter=0
fname = input("Enter file name: ")
fh = open(fname)
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
     
    counter=counter+1
    pos=line.find(':')
    val=line[pos+1:]
    tot=tot+float(val)
    avg=tot/counter
print("Average spam confidence:",avg)