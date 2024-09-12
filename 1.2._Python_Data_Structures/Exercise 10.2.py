#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  1 11:59:04 2023

@author: josemanuelplaza
"""

name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

hour_counts = dict()

for line in handle:
    if line.startswith("From "):
        words = line.split()
        if len(words) > 5:
            time = words[5]
            hour = time.split(":")[0]
            hour_counts[hour] = hour_counts.get(hour, 0) + 1

sorted_hours = sorted(hour_counts.items())

for hour, count in sorted_hours:
    print(hour, count)