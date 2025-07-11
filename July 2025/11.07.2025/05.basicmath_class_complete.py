class BasicMaths:
    def __init__(self, a, b):
        self.a=a
        self.b=b

    def add(self):
        return(f"The total sum is {self.a + self.b}")
    
    def substraction(self):
        return(f"The substraction of a and b is:{self.a - self.b}")
    
    def multiply(self):
        return(f"The result of the multiplying is: {self.a * self.b}")
    
    def division(self):
        return(f"The divison of a and b is:{self.a / self.b}")
    
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

    def absolute(self):
        abs_a = self.a if self.a >= 0 else -self.a
        abs_b = self.b if self.b >= 0 else -self.b
        return f"Absolute value of {self.a} is {abs_a}, of {self.b} is {abs_b}"
    
    def rounding(self):
        integer_no= int(self.a)
        decimal_part=self.a-integer_no
        if decimal_part <0.5:
            return(f"the rounded number of {self.a} is {integer_no}")
        else:
            return(f"the rounded number of {self.a} is {integer_no+1}")
    
    def square_roots(self):
        if self.a < 0 or self.b < 0:
            return "Error: Cannot take square root of negative number."
        else:
            return f"Square root of {self.a} is {self.a ** 0.5}, of {self.b} is {self.b ** 0.5}"
    
    
    def minimum_and_maximum(self):
        if self.a < self.b:
            return(f"Number{self.a} is smaller than number {self.b}")
        elif self.a==self.b:
            return(f"The number {self.a} and number {self.b} are equal")
        else:
            return(f"Number {self.a} is bigger than number {self.b}")

number1 = float(input("Enter first number:\n"))
number2 = float(input("Enter second number:\n"))

result = BasicMaths(number1, number2)

print(result.add())
print(result.substraction())
print(result.multiply())
print(result.division())
print(result.integer_division())
print(result.modulo())
print(result.power())
print(result.even_odd())
print(result.absolute())
print(result.rounding())
print(result.square_roots())
print(result.minimum_and_maximum())