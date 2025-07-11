# Exercise 1: Even or Odd
# Write a Python program that:
# Asks the user for a number.
# Checks whether the number is even or odd using the % operator.
# Displays an appropriate message:
# "The number is EVEN." if the number is even.
# "The number is ODD." if the number is odd.

def even_or_odd():
    number=int(input("please add any number\n"))
    if number % 2==0:
        return("The number is even")
    else:
        return("The number is ODD")
        

print(even_or_odd())


