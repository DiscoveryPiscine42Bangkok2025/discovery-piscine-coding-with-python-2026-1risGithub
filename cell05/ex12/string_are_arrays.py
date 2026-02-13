#!/usr/bin/env python

import sys

if len(sys.argv) != 2:
    print("none")
else:
    count = sys.argv[1].count("z")
    print("z" * count if count > 0 else "none")