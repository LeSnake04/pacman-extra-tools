#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from contentdb import GetContent


def parsecmdinfo():
    commands = GetContent()['commands']
    output = """After having to search for many pacman hidden functions myself, i decided to help others by giving them by giving them an easy way to use the functions i found.
If you dont trust my program want to use the functions directly instead, you more are welcome to copy the lines from here:

"""
    for k, v in commands.items():
        output += k + ": " + v + "\n"
    print(output)
