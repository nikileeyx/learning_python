
'''
Using a for loop, write an iterative function sum_odd_n that computes the sum of the first n odd numbers, 
i.e. it returns 1 + 3 + 5 + .... + (2n - 1). You may assume that n is always a positive integer.
'''

def sum_odd_n(n):
    listit = []
    total= 0
    
    max = 2 * n - 1
    
    for num in range(1,max+1):
        listit.append(num)

    for i in range(1,max+1,2):
        total = total + i


    return total
