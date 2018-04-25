# -*- coding: utf-8 -*-
"""
Created on Wed Apr 25 16:15:44 2018

@author: dhoop
"""

import sys

player1 = input("Enter Player 1's Name: ")
player2 = input("Enter Player 2's Name: ")
player1_choice = input("Rock, Paper, or Scissors %s? " % player1)
player2_choice = input("Rock, Paper, or Scissors %s? " % player2)

def player(p1, p2):
    if p1 == p2:
        return("Tie!")
        
    elif p1 == "Rock" or p1 == "rock":
        if p2 == "Scissors" or p2 == "scissors":
            return ("%s Wins!" % player1)
        else:
            return ("%s Wins!" % player2)
        
    elif p1 == "Scissors" or p1 == "scissors":
        if p2 == "Paper" or p2 == "paper":
            return ("%s Wins!" % player1)
        else:
            return ("%s Wins!" % player2)
        
    elif p1 == "Paper" or p1 == "Paper":
        if p2 == "Rock" or p2 == "rock":
            return ("%s Wins!" % player1)
        else:
            return ("%s Wins!" % player2)
        
    else:
        return("You must choose Rock, Paper, or Scissors! No Cheating!")
        sys.exit()
        
print(player(player1_choice, player2_choice))
        
    
    