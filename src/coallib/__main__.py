#!/usr/bin/env python3
# Made by @Ericwasepic127

from .termtool import confirm, MODE_YN
from . import loady

if __name__ == '__main__':
    print("Welcome to @Ericwasepic127 library!")
    print("Name Coallib made from Minecraft [Coal] + Python [Lib]rary")
    print("Version: 1.0\nThanks for using my library!")
    if confirm("Would you rather open help for loady project?", mode=MODE_YN):
        help(loady)
