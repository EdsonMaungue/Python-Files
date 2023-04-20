# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 19:07:01 2023

@author: Edson
"""

# a function that takes a list and target parameter
# multiple variables : middle, start, end, steps
# recursion or while loop
# increase the steps each time a split is done
# conditions to track target position

 
def binary_search(List, element):
    middle = 0
    start = 0
    end = len(List)
    steps = 0
    
    while(start<=end):
        print("Step",steps,":",str(List[start:end+1]))
        
        steps = steps+1
        middle = (start + end) // 2
        
        if element == List(middle):
            return middle
        if element < List(middle):
            end = middle -1
        else:
            start = middle + 1
            
    return -1

my_list = [1,2,3,4,5,6,7,8,9,10,11,12]
target = 12

binary_search(my_list, target)