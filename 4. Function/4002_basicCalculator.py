
'''
LYNXdigital
This is a simple calculator with two functions. 
There are three inputs from the user, two operands and one operator
'''

def addition(x,y):
    add = 0
    addVal = int(x) + int(y)
    return addVal

def subtraction(x,y):
    sub = 0
    subVal = int(x) - int(y)
    return subVal

numOne = input("Input a first number: ")
numTwo = input("Input a second number: ")
funcChoose = input("Input a function: (add/sub) ")

if funcChoose == "add":
    print(addition(numOne, numTwo))

else:
    print(subtraction(numOne, numTwo))
