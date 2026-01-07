def number_inputs():
    a=float(input("Enter first number: "))
    b=float (input ("Enter second number: "))
    return a,b


def add_numbers(a,b):
    return a+b

def multiply_numbers(a,b):
    return a*b

def divide_numbers(a,b):
    return float(a/b)

def subtract_numbers(a,b):
    return a-b


x,y=number_inputs()

sum = add_numbers(x,y)
difference=subtract_numbers(x,y)
product=multiply_numbers(x,y)
division=divide_numbers(x,y)
print("Sum =", sum)
print("Difference=",difference)
print("Product=",product)
print("Division=",division)

