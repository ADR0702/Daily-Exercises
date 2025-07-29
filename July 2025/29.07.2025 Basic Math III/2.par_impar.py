# user=int(input("Please enter a number: \n"))

# if user/2== 0:
#     print("The number is even ")
# else:
#     print("The number is odd")

def even_odd(user):
    if user%2== 0:
        print("The number is even ")
    else:
        print("The number is odd")

number=int(input("Please enter a number: \n"))

even_odd(number)
