#Exercise 3 – Square Root (Without math.sqrt)
# Task:
# Ask the user to enter a positive number (float or int).
# Calculate the square root of the number using the exponent operator (**).
# Print the result.

def square_roots(x):
    if x<0:
        return ("Error: This is a negative number. Please add a positive number")
    else:
        return(f"The Square Root of {x} is : {x **0.5}")

number=float(input("please insert a number\n"))

print(square_roots(number))

# built in version

import math
rootnumber=float(input("please insert a number\n"))
print(f"The Square Root of {rootnumber} is : {math.sqrt(rootnumber)} ")
