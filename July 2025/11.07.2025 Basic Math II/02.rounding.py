# Exercise 2 – Rounding a Decimal Number
# Task:
# Write a Python program that:
# Asks the user to enter a decimal number (a float).
# Displays:
# The result of normal rounding 
# The result of rounding up 
# The result of rounding down 

def rounding(a):
    integer_no= int(a)
    decimal_part=a-integer_no
    if decimal_part <0.5:
        return(f"the rounded number of {a} is {integer_no}")
    else:
        return(f"the rounded number of {a} is {integer_no+1}")
    
number=float(input("please insert a number\n"))
print(rounding(number))

# built in version

import math

added_number=float(input("please insert a number\n"))
round(added_number)
print(f"rounded up result is : {math.ceil(added_number)}")
print(f"rounded down result is :{math.floor(added_number)}")