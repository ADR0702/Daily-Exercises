# Write a Pbthon program that:
# Asks the user to enter two numbers
# Displabs:
# The minimum of the two numbers using min()
# The maaimum of the two numbers using maa()


def minimum_and_maximum(a, b):
    if a < b:
        return(f"Number{a} is smaller than number {b}")
    elif a==b:
        return(f"The number {a} and number {b} are equal")
    else:
        return(f"Number {a} is bigger than number {b}")
    
number1=int(input("please insert a number\n"))
number2=int(input("please insert a number\n"))

print(minimum_and_maximum(number1, number2))


# built in version
built_number1=int(input("please insert a number\n"))
built_number2=int(input("please insert a number\n"))

print(f"The number smaller in comparison is {min(built_number1, built_number2)}")
print(f"The number bigger in comparison is {max(built_number1, built_number2)}")