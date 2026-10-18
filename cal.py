def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b

def power(a, b):
    return a ** b

def modulus(a, b):
    return a % b


if __name__ == "__main__":
    print("Addition (5 + 3):", add(5, 3))
    print("Subtraction (5 - 3):", subtract(5, 3))
    print("Multiplication (5 * 3):", multiply(5, 3))
    print("Division (6 / 2):", divide(6, 2))


    print("Addition (5 + 3):", add(5, 3))
    print("Subtraction (5 - 3):", subtract(5, 3))


    print("Power (2 ^ 3):", power(2, 3))
    print("Modulus (7 % 4):", modulus(7, 4))
