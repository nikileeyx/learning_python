
'''
Using the square and mean functions, 
- define a new function called variance that calculates the variance of two input parameters
- deuse the square and mean functions

'''

def square(x):
    return x * x

def mean(x, y):
    return (x + y) / 2

def variance(x, y):
    mean_xy = mean(x,y)
    square_x = square(x)
    square_y = square(y)

    return ((square_x) + (square_y))/2 - (mean_xy)**2

