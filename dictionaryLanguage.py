#Guessing Number Game 1.0 by @codingLYNX

'''
Given the cosmopolitan society we live in, many of us speak several different languages.

This function named greet can:
1. takes in a person's name and language, 
2. returns a different greeting string depending on which language is given and include the person's name behind it.

Note: Do not use the command print to print the greeting, greet should be return a string.

You are free to include additional languages but minimally, for grading purposes, 
please support the following 3 languages: English, Klingon and Elvish.
'''

greeting = 0

def greet(name, language):
    
    greetingLanguage = {"English": "Nice to meet you" , "Klingon": "nuqneH", "Elvish": "Gi suilon"}
    greetMe = greetingLanguage.get(language)
    greeting = greetMe + " " + name

    print(greeting)

    return greeting


greet("Niki", "English")
