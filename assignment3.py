#Task 1: Calculate Factorial Using a Function
def factorial(num):
    if num<1:
        return 1
    else:
        return num*(factorial(num-1))

n=int(input("Enter a number "))
result=factorial(n)
print("The factorial of",n,"is",result)



# Task 2: Using the Math Module for Calculations

from math import *
n=int(input("Enter a number "))
print("Square root of ",n,"is",sqrt(n))
print("Logarithm value of  ",n,"is",log(n))
print("Sine : ",sin(n))