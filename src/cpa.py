#!/usr/bin/env python3

import sys
import json

import app

def main():
    """The entry point for the program

    """
    args = sys.argv[1:]

    if not args:
        print("USAGE: ./cpa.py [PATHS]")

    for arg in args:
        app.process_path(arg)

if __name__ == "__main__":
    main()
