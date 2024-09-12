#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  5 13:40:21 2023

@author: josemanuelplaza
"""

import re

filename = r"/Users/josemanuelplaza/Desktop/regex_sum_1853645.txt"

with open(filename, 'r') as file:
    content = file.read()

# Find all integers in the content using regular expression '[0-9]+'
numbers = re.findall(r'[0-9]+', content)

# Convert the extracted strings to integers and sum them up
total_sum = sum(map(int, numbers))

print(total_sum)
