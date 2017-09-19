# -*- coding: utf-8 -*-
"""
Created on Thu Sep  7 23:34:22 2017

@author: user
"""
""" this is just the draft"""
# Group 7
# Reyes Ceballos and Sen Varghese
# 9/22/2017
# Homework 1
# I am a three-digit number.
# My tens digit is 5 more than my ones digit.
# My hundreds digit is 8 less than my tens digit.
# What number am I?


answer = 194

# starts the game
#Question

guess = eval(input('Please enter an integer: '))
 
if guess == answer:
    print('That is correct! You win! ')
if guess != answer:
    print('Wrong! You lose!')
if guess < answer:
    print('Guess higher next time!')
if guess > answer:
    print('Guess lower next time!')
    
print('Goodbye ')

# End of game. Re-run to play again.
    
