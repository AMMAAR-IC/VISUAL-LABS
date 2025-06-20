# Assigning integer values to variables
num1 = 10
num2 = 20

# 1. Arithmetic Operators
print("Arithmetic Operators:")
print(num1 + num2)       # Addition → 30
print(num1 - num2)       # Subtraction → -10
print(num1 * num2)       # Multiplication → 200
print(num1 / num2)       # Division → 0.5
print(num1 % num2)       # Modulus → 10
print(num1 ** 2)         # Exponentiation → 100
print(num2 // num1)      # Floor Division → 2

# Chaining arithmetic operators with BODMAS
print((num1 + num2) * (num1 - num2))  # (10+20)*(10-20) → 30 * -10 → -300

# 2. Relational (Comparison) Operators
print("\nRelational Operators:")
print(num1 == num2)      # False
print(num1 != num2)      # True
print(num1 > num2)       # False
print(num1 < num2)       # True
print(num1 >= 10)        # True
print(num2 <= 30)        # True

# 3. Logical Operators
print("\nLogical Operators:")
a = True
b = False
print(a and b)           # False
print(a or b)            # True
print(not a)             # False

# 4. Assignment Operators
print("\nAssignment Operators:")
x = 5
x += 3                   # x = x + 3 → 8
print(x)
x *= 2                   # x = x * 2 → 16
print(x)

# 5. Bitwise Operators
print("\nBitwise Operators:")
print(num1 & num2)       # AND → 0
print(num1 | num2)       # OR → 30
print(num1 ^ num2)       # XOR → 30
print(~num1)             # NOT → -11
print(num1 << 2)         # Left shift (multiply by 4) → 40
print(num2 >> 1)         # Right shift (divide by 2) → 10

# 6. Membership Operators
print("\nMembership Operators:")
text = "python"
print("p" in text)       # True
print("z" not in text)   # True

# 7. Identity Operators
print("\nIdentity Operators:")
a = [1, 2, 3]
b = a
c = [1, 2, 3]
print(a is b)            # True (same object)
print(a is c)            # False (same content, different object)
print(a == c)            # True (same values)
