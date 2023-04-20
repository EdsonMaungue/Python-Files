# -*- coding: utf-8 -*-
"""
Created on Tue Apr  4 16:38:38 2023

@author: Edson
"""

import random

exit = False
user_points = 0
computer_points = 0

while exit == False:
    options = ["rock", "paper", "scissors"]
    user_input = input("Choose rock, paper, scissors or exit: ")
    computer_input = random.choice(options)
    
    if user_input == "exit" or user_input == "Exit":
        print("Game ended")
        print("You won a total score of "+ str(user_points) + " and the computer total score is "+ str(computer_points))
        exit = True
        
    if user_input == "rock" or user_input == "Rock":
        if computer_input == "rock" or computer_input == "Rock":
            print("Your input is rock")
            print("Computer input is rock")
            print("It is a tie!")
        elif computer_input == "paper" or computer_input == "Paper":
            print("Your input is rock")
            print("Computer input is paper")
            print("Computer WINS")
            computer_points += 1
        elif computer_input == "scissors" or computer_input == "Scissors":
            print("Your input is rock")
            print("Computer input is scissors")
            print("You WIN")
            user_points += 1
    elif user_input == "paper" or user_input == "Paper":
        if computer_input == "rock" or computer_input == "Rock":
            print("Your input is paper")
            print("Computer input is rock")
            print("You WIN!")
            user_points += 1
        elif computer_input == "paper" or computer_input == "Paper":
            print("Your input is paper")
            print("Computer input is paper")
            print("It's a Tie!")
        elif computer_input == "scissors" or computer_input == "Scissors":
            print("Your input is paper")
            print("Computer input is scissors")
            print("Computer WINS!")
            computer_points += 1
    elif user_input == "scissors" or user_input == "Scissors":
        if computer_input == "rock" or computer_input == "Rock":
            print("Your input is scissors")
            print("Computer input is rock")
            print("Computer Wins!")
            computer_points += 1
        elif computer_input == "paper" or computer_input == "Paper":
            print("Your input is scissors")
            print("Computer input is paper")
            print("You WIN!")
            user_points += 1
        elif computer_input == "scissors" or computer_input == "Scissors":
            print("Your input is scissors")
            print("Computer input is scissors")
            print("It's a Tie!")
            
    elif user_input != "rock" or user_input != "Rock" or user_input != "paper" or user_input != "Paper" or user_input != "scissors" or user_input != "Scissors":
        print("Invalid Options")
           
        