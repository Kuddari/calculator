"""
Program: Simple Calculator 
Author: Anas Tawalbeh
Simple calcuatro help the user calculate the basic 4 operations including:
addition, subtraction, multiplication and division
Significant constants
         there is no constants
 2. The inputs are
         2 numbers (at least)
 3. Computations:
         addition: number + another number
         subtraction: number - another number
         multiplication: number * another number
         division: number / another number
 4. The outputs are
         computation result
"""

number1=int(input("Insert the first value"))
number2=int(input("Insert the second value"))

addition=number1+number2
print(f"The sumation for the two values is equal to: ,{addition}")

subtraction=number1-number2
print(f"The sumation for the two values is equal to: ,{subtraction}")

multiplication=number1*number2
print(f"The sumation for the two values is equal to: ,{multiplication}")

division=number1/number2
print(f"The sumation for the two values is equal to: ,{division}")
