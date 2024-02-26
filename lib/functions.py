#!/usr/bin/env python3

def greet_programmer():
    print("Hello, programmer!")


def greet(name):
    print(f"Hello, {name}!")

 

def greet_with_default(name="programmer"):
     print(f"Hello, {name}!")


     

def add(num1, num2):
    return num1 + num2

result3 = add(3, 1);
print(result3)



def halve(number):
    if type(number) in (int, float):
        return number / 2
    else:
        return None

result4 = halve(6)
print(result4)