#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 23 14:41:19 2023

@author: josemanuelplaza
"""

score = input("Enter Score: ")

try:
    score = float(score)
except:
    score = -1

if score >= 0.9:
    print("A")
elif score >= 0.8:
    print("B")
elif score >= 0.7:
    print("C")
elif score >= 0.6:
    print("D")
elif score < 0.6:
    print("F")
else:
    print("Error!")
    quit()