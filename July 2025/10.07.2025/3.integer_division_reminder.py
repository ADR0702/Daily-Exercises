# Write a Python program that:
# Asks the user to input two integers (a and b);
# Displays:
# the result of the integer division a // b;
# the remainder of the division a % b.

def integer(a, b):
    return a//b
number1 = int(input("Enter first number:\n"))
number2 = int(input("Enter second number:\n"))

integer_result=integer(number1, number2)
print(integer_result)


def reminder(a, b):
    return a%b
number1 = int(input("Enter first number:\n"))
number2 = int(input("Enter second number:\n"))

reminder_result=reminder(number1, number2)
print(reminder_result)

# simplified
def reminder(a, b):
    return a%b

def integer(a, b):
    return a//b

number1 = int(input("Enter first number:\n"))
number2 = int(input("Enter second number:\n"))

reminder_result=reminder(number1, number2)
integer_result=integer(number1, number2)

print(integer_result)
print(reminder_result)