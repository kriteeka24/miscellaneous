def get_numbers():
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    return a, b


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "Undefined (division by zero)"
    return a / b


x, y = get_numbers()

print(f"Sum         = {add(x, y)}")
print(f"Difference  = {subtract(x, y)}")
print(f"Product     = {multiply(x, y)}")
print(f"Division    = {divide(x, y)}")
