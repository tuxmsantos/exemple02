#!/usr/bin/env python

def sum_numbers(first, second):
    return first + second

def multiply_numbers(first, second):
    return first * second

def divide_numbers(first, second):
    return first // second

def subtract_numbers(first, second):
    return first - second
    
firstNumber = input("Enter with the first number: ")
secondNumber = input("Enter with the second number: ")


print("The Sum result is......: {}".format(sum_numbers(int(firstNumber),int(secondNumber))))
print("The Multiplication is..: {}".format(multiply_numbers(int(firstNumber),int(secondNumber))))
print("The Division is .......: {}".format(divide_numbers(int(firstNumber),int(secondNumber))))
print("The Subtraction is ....: {}".format(subtract_numbers(int(firstNumber),int(secondNumber))))



