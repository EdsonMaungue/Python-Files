# -*- coding: utf-8 -*-
"""
Created on Sat Apr  1 11:00:30 2023

@author: Edson
"""

# have a python dicitonary that has a key/value pair that represents a word and it's definition
# collect input from the user, input is a word
# check if the word is in the dictionary
# print the definition

from PyDictionary import PyDictionary

dictionary = PyDictionary("eyes", "indentation", "head")


print(dictionary.getMeanings())