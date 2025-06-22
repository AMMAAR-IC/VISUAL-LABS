# Demonstrates: try-except, multiple exceptions, custom exception

def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: Cannot divide by zero!"
    except TypeError:
        return "Error: Invalid input types!"

print(divide(10, 2))
print(divide(10, 0))
print(divide(10, "a"))

# Custom exception
class NegativeNumberError(Exception):
    pass

def check_positive(n):
    if n < 0:
        raise NegativeNumberError("Negative number not allowed.")
    return "All good!"

try:
    print(check_positive(-5))
except NegativeNumberError as e:
    print("Custom Error:", e)
