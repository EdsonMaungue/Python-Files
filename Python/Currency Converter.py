# -*- coding: utf-8 -*-
"""
Created on Sat Apr  1 10:47:00 2023

@author: Edson
"""

def main():
    print("This program converts US dollars to Metical")
    print()
    
    dollars = eval(input("Enter amount in dollars: "))
    
    pounds = convert_to_pounds(dollars)
    
    print("That is ", pounds, " Pounds.")
    
convert_to_pounds = lambda dollars: dollars * 65.2

main()
    
    