# Absolute Value
# Write a function that takes a number from the user and prints its absolute value using abs().

def absolute(a):
    if a < 0:
        return(f"Valoarea absoluta a lui {a} este: {-a}")
    else:
        return (f"Valoarea absoluta a lui {a} este: {a}")
    
numar=int(input("introduceti un numar\n"))

print(absolute(numar))

# built in option:
print(abs(-300))