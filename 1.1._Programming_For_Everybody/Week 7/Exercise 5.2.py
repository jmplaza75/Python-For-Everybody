#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 23 13:11:07 2023

@author: josemanuelplaza
"""


largest = None
smallest = None

while True:
    num = input("Enter a number: ")
    if num == "done" : 
        break
    try:
        num = int(num)
    except:
        print ("Invalid input")
        continue
    if smallest is None:
        smallest = num
    if (largest is None):
        largest = num
    if num > largest:
        largest = num
    if num < smallest :
        smallest = num


print ("Maximum is", largest)
print ("Minimum is", smallest)