# -*- coding: utf-8 -*-
"""
Created on Wed Apr 25 16:31:10 2018

@author: dhoop
"""

import sys
import random

ranum = random.randint(1, 10)

def play():
    playing = True
    while playing:
        num = int(input("Enter a number between 1 and 9: "))
        if num > ranum:
            print("%s is too high. Try again." % num)
            playing = True
        elif num < ranum:
            print("%s is too low. Try again." % num)
            playing = True
        elif num == ranum:
            print("%s is right! Congrats!" % num)
            playing = False
        else:
            print("That's not a number...")
            sys.exit()

play()