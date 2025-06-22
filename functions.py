# Demonstrates: basic functions, parameters, return, recursion
 
def greet(name):
    return f"Hello, {name}!"

def add(a, b):
    return a + b

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print(greet("Ammaar"))
print("5 + 3 =", add(5, 3))
print("Factorial of 5:", factorial(5))
