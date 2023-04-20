# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 19:34:51 2023

@author: Edson
"""

# a dicitionary that stores questions and answers
# have a variable that tracks the score of the player
# Loop through the dictinary using the key values pairs
# display each question to the user and allow them to answer
# tell them if they are right or wrong
# show the final result when quiz is completed


quiz = {
     "question1": {
         "question": "what is the capital of France?",
         "answer": "Paris"
         
     },
     "question2": {
         "question": "what is the capital of Germany?",
         "answer": "Berlin"
     },
     "question3": {
         "question": "what is the capital of Italy?",
         "answer": "Rome"
         
     },
     "question4": {
         "question": "what is the capital of Spain?",
         "answer": "Madrid"
     },
     "question5": {
         "question": "what is the capital of Portugal?",
         "answer": "Lisbon"
         
     },
     "question6": {
         "question": "what is the capital of Switzerland?",
         "answer": "Bern"
     },
     "question7": {
         "question": "what is the capital of Austria?",
         "answer": "Vienna"
         
     },
     "question8": {
         "question": "what is the capital of Mozambique?",
         "answer": "Maputo"
     },
     "question9": {
         "question": "what is the capital of Brazil?",
         "answer": "Brasilia"
         
     },
     "question10": {
         "question": "what is the capital of USA?",
         "answer": "Washinton DC"
     },
     "question11": {
         "question": "what is the capital of South Africa?",
         "answer": "Journaburg"
         
     },
     "question12": {
         "question": "what is the capital of Angola?",
         "answer": "Luanda"
     },

 }

score = 0

for key, value in quiz.items():
    print(value['question'])
    answer = input("Answer? ")
    
    if answer.lower() == value['answer'].lower():
        print('Correct')
        score = score + 1
        print("Your score is: " + str(score))
        
    else:
        print("Wrong!")
        print("The answer is: "+ value['answer'])
        print("Your score is: " + str(score))
        print("")
        print("")
        
print("You got " + str(score) + " out of 12 questions correctly")
print("Your percentage is " + str(int(score/12 * 100)) + "%")



