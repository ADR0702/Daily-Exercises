class BasicMaths:
    def __init__(self, a, b):
        self.a=a
        self.b=b

    def add(self):
        return(f"the toal sum is {self.a + self.b}")
    
    def substraction(self):
        return(f" the substraction of a and b is:{self.a - self.b}")
    
    def multiply(self):
        return(f"the result of the multiplying is: {self.a * self.b}")
    
    def division(self):
        return(f" the divison of a and b is:{self.a / self.b}")
    
    def integer_division(self):
        return(f"The remainder is{self.a // self.b}")
    
    def modulo (self):
        return(f"The result of integer division is:{self.a % self.b}")
    
    def power(self):
        return(f"The result of exponentiation is:{self.a ** self.b}")
    
    def even_odd(self):
        if self.a % 2==0 and self.b % 2==0:
            return("The number is even")
        else:
            return("The number is ODD")
        

number1 = int(input("Enter first number:\n"))
number2 = int(input("Enter second number:\n"))

result=BasicMaths(number1, number2)
print(result.add())
print(result.substraction())
print(result.multiply())
print(result.division())
print(result.integer_division())
print(result.modulo())
print(result.even_odd())
