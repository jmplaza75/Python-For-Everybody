#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 30 09:03:49 2023

@author: josemanuelplaza
"""

fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    for i in line.split():
        if not i in lst:
            lst.append(i)
lst.sort()
print(lst)