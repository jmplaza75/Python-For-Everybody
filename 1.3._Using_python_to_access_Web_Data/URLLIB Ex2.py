#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  7 17:29:01 2023

@author: josemanuelplaza
"""

from urllib import request
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


url = input("Enter URL: ")
count = int(input("Enter count: "))
position = int(input("Enter position: "))

names = []

for _ in range(count):
    print("retrieving: {0}".format(url))
    html = request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, "html.parser")
    anchors = soup('a')
    name = anchors[position - 1].string
    names.append(name)
    url = anchors[position - 1]['href']

print(names[-1])
