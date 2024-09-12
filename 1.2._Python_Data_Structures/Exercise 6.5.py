#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 25 08:08:08 2023

@author: josemanuelplaza
"""

text   = "X-DSPAM-Confidence:    0.8475"
num = float(text[text.find('0') : ])
print (num)