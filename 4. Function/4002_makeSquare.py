

'''
Define a function area_square(x) that:
Returns the area of a square of length x. The area_square function should make use of the area_rect function. 
Thus, you do not need to know how the area of a rectangular is calculated.
Returns 0 if the input parameter is <= 0.
'''

def area_square(a):
    area = 0
    if a > 0:
        area = area_rect(a,a)
    else:
        area = 0
    return area
    
def area_rect(x,y):
    area = x * y
    return area
    

