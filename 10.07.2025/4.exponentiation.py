#  Write a Python program that:
# Asks the user for two numbers:
# one base number
# one exponent
# Calculates and displays the result of raising the base to the power of the exponent (base ** exponent).

def exponentiation(a, b):
    return a ** b
base_number= int(input("Enter first number:\n"))
the_exponent = int(input("Enter second number:\n"))

exponentiation_result=exponentiation(base_number, the_exponent)

print(exponentiation_result)

