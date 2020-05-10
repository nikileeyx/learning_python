
'''
Rewrite your pay computation to give the employee 1.5 times the hourly rate for hours worked above 40 hours.

Here's an example:
Enter Hours: 45
Enter Rate: 10
Pay: 475.0
'''


workaholic = int(input("How long have you been working for? (in hours) "))
perHour = int(input("What's your pay per hour? "))
moolah = 0

if int(workaholic) > 40:
    moolah = perHour * workaholic * 1.5

else:
    moolah = perHour * workaholic

print("Your tragic pay is $" + str(moolah))
    
