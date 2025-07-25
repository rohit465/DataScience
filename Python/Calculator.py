def Square(n):
    return n**2

def Cube(n):
    return n**3

def factorial(n):
    if(n==1 or n==0):
        return 1
    return n*factorial(n-1)

def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    if b==0:
        return "Can't divide by 0"
    return a/b