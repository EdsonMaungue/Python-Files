# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 17:53:11 2023

@author: Edson
"""

def replace_word():
    
    str = "Hi guys, I am Edson, and hi hi hi hi"
    word_to_replace = input("Enter the word to replace: ")
    word_replacement = input("Enter the word replacement: ")
    print(str.replace(word_to_replace, word_replacement))
    
replace_word()