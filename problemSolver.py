import math

"""Returns x"""
def f(x):
    return x ** 2 - 2 * x


def g(x):
    arr = []
    for i in range(x):
        arr.append(x ** 2)
    return arr


def getHigher(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2


def greetUser():
    print("Hello! How is your day?")