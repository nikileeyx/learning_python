
'''
Guessing Number Game 1.0 by @codingLYNX
Contact me at t.me/nikileeyyxx

This code features a guessing number game using a simple function.
 - Guess a number from 1 to 10
 - Infinite number of guesses
 - Game ends when you guess the number correctly!

'''

# Firstly, declare all your global variables here

completed = 0


# Secondly, you define all your functions that you want to use

def checkNumbers(guessNumber):
    luckyNumber = 10
    if str(my_guess) == str(luckyNumber):
        print("You're right! The number is " + str(luckyNumber) + "!")
        completed = 0
    else:
        print("Try again!")
        completed = 1

    return completed



# At last! This is the executable code!

if completed == 1:
    while completed == 0:
        my_guess = input("Choose a number from 1 to 10! ")
        checkNumbers(my_guess)
