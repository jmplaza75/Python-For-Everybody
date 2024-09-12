#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  7 17:11:41 2023

@author: josemanuelplaza
"""

import urllib.request
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL: ')
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})

try:
    with urllib.request.urlopen(req, context=ctx) as response:
        html = response.read()
        soup = BeautifulSoup(html, 'html.parser')
        numbers = [int(span.string) for span in soup('span')]
        print(sum(numbers))
except urllib.error.URLError as e:
    print(f"Failed to retrieve data from {url}: {e}")
