# -*- coding: utf-8 -*-
"""
Created on Sat Apr  1 09:48:30 2023

@author: Edson
"""

# Ask user if they want to generate a password or not
# If yes, ask for password length
# Generate password
# Print password
# If initial response is no, exit program

import string
import random

characters = list(string.ascii_letters + string.digits + "abcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()")

def generate_password():
    password_length = int(input("How long would you like your password to be? "))
    
    random.shuffle(characters)
    
    password = []
    
    for x in range(password_length):
        password.append(random.choice(characters))
        
    random.shuffle(password)
    
    
    password = "".join(password)
    
    print(password)
    
option = input ("Do you want to generate a password? (Yes/No): ")

if option == "Yes" or option == "yes":
    generate_password()
elif option == "No" or option == "no":
    print("program ended")
    quit()
else:
    print("Invalid input, please input Yes or No")
    quit()