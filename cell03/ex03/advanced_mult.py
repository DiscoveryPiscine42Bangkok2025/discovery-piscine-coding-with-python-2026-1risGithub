#!/usr/bin/env python

import sys

if len(sys.argv) > 1:
    print("none")
else:
    for i in range(11):
        print("Table de", i, end=": ")
        for j in range(11):
            print(i * j, end=" ")
        print()