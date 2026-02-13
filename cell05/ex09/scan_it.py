#!/usr/bin/env python

import sys

args = sys.argv[1:]

if len(args) != 2:
    print("none")
else:
    keyword = args[0]
    sentence = args[1]
    count = sentence.count(keyword)

    if count == 0:
        print("none")
    else:
        print(count)