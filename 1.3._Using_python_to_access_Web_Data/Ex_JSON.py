#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 10 17:51:15 2023

@author: josemanuelplaza
"""

import urllib.request as ur
import json

def main():
    json_url = input("Enter a valid JSON URL: ")
    
    try:
        print("Retrieving", json_url)
        data = ur.urlopen(json_url).read().decode('utf-8')
        print('Retrieved', len(data), 'characters')
        
        json_obj = json.loads(data)

        if 'comments' in json_obj:
            comments = json_obj['comments']
            total_number = len(comments)
            sum_counts = sum(comment['count'] for comment in comments)
            print('Count:', total_number)
            print('Sum:', sum_counts)
        else:
            print('Invalid JSON format. No "comments" key found.')

    except ValueError as e:
        print("Invalid JSON:", e)
    except urllib.error.URLError as e:
        print("URL Error:", e)
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    main()
