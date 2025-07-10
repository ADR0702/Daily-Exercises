import operator

# Way 1: Basic version
number = int(input("Please enter a number:\n"))
number2 = int(input("Please enter another number:\n"))

basic_sum = number + number2
basic_product = number * number2

print("Basic sum:", basic_sum)
print("Basic product:", basic_product)

# Way 2: Using functions

def get_sum(a, b):
    return sum([a, b])

def get_product(a, b):
    return operator.mul(a, b)

number1 = int(input("Enter first number:\n"))
number2 = int(input("Enter second number:\n"))

addition = get_sum(number1, number2)
multiplication = get_product(number1, number2)

print("The sum is:", addition)
print("The product is:", multiplication)
