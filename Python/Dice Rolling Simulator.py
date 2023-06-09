# -*- coding: utf-8 -*-
"""
Created on Sat Apr  1 10:22:45 2023

@author: Edson
"""

# import random
# define a function to roll the dice
# create a dictionary that will have the drawings of the dice
# create a dictionary that will values of the dice


import random


def roll_dice():
    
    dice_drawing = {
       1: (
        "┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘",
       ),
       2: (
        "┌─────────┐",
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└─────────┘",
        ),
       3: (
        "┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘",
        ),
       4: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘",
        ),
       5: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘",
        ),
       6: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘",
        ),
       
    }
    
    roll = input("Roll the dice? (Yes/No): ")
    
    while roll.lower() == "Yes".lower():
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        
        print("dice rolled: {} and {}".format(dice1, dice2))
        print("\n".join(dice_drawing[dice1]))
        print("\n".join(dice_drawing[dice2]))
        
        
        roll = input("Roll again (Yes/No): ")
    
    
roll_dice()