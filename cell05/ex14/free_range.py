#!/usr/bin/env python

import sys

if len(sys.argv) != 3:
    print("none")
else:
    start = int(sys.argv[1])
    end = int(sys.argv[2])
    print(list(range(min(start, end), max(start, end) + 1)))
