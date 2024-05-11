#import modules
import os
import random
import sys

#variables
goal = random.randint(1, 100)
guess = 0
correctniss = 0 #0 means too low and 1 means too high and 2 means correct
number_of_tries = 11
#clear screen
os.system('clear')

#functions
def guess_check(guess, goal):
    if guess > goal:
        correctniss = 1
        print("Too high")
    if guess < goal:
        correctniss = 0
        print("Too low")
    if guess == goal:
        correctniss = 2
        print("you are Correct")
        sys.exit()

    return 

#intro
print("Welcome to Number Guessing Game")
print("I am thinking of a number between 1 and 100")
print("You its your job to get the correct number")
print("you have", number_of_tries - 1, "tries to get the correct number")
print("start guessing your first number")
for i in range(0, number_of_tries):
    guess = int(input())
    guess_check(guess, goal)
print("you lose")



