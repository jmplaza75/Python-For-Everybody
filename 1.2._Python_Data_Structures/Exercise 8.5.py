#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 30 10:43:01 2023

@author: josemanuelplaza
"""

fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"

fh = open(fname)
count = 0

for line in fh:
    line.rstrip()
    if line.startswith("From: "):
        words = line.split()
        print(words[1])
        count += 1

print("There were", count, "lines in the file with From as the first word")
