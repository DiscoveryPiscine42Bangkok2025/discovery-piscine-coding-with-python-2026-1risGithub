#!/usr/bin/env python

import sys
from checkmate import checkmate

def load_board(filename):
    with open(filename, "r") as f:
        content = f.read()
    return content


def main():
    if len(sys.argv) < 2:
        print("Error")
        return

    for filename in sys.argv[1:]:
        try:
            board = load_board(filename)
            checkmate(board)
        except Exception:
            print("Error")


if __name__ == "__main__":
    main()
