#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  8 11:22:19 2023

@author: josemanuelplaza
"""

import urllib.request as ur
import xml.etree.ElementTree as et

def main():
    url = input('Enter location: ')

    try:
        print('Retrieving', url)
        xml = ur.urlopen(url).read()
        print('Retrieved', len(xml), 'characters')

        tree = et.fromstring(xml)
        counts = tree.findall('.//count')

        total_number = 0
        sum_ = 0

        for count in counts:
            sum_ += int(count.text)
            total_number += 1

        print('Count:', total_number)
        print('Sum:', sum_)

    except Exception as e:
        print('An error occurred:', e)

if __name__ == "__main__":
    main()
