#The Code Reusing 1.0 by @codingLYNX
'''
Note: In this question, 0 is considered to be neither a positive number nor negative number.

You are to implement the following three functions with the following specifications:
is_odd(x) returns True if the input parameter x is odd, False otherwise.
is_negative(x) returns True if the input parameter x is negative, False otherwise.
is_even_and_positive(x) returns True if the input parameter x is even AND positive, False otherwise.
'''

def is_odd(x):
    if x%2 == 0:
        return False
    else:
        return True
        
def is_negative(x):
    if x < 0:
        return True
    else:
        return False
    
def is_even_and_positive(x):
    
    if x == 0:
        return False
        
    elif is_odd(x) or is_negative(x):
        return False
        
    else:
        return True
