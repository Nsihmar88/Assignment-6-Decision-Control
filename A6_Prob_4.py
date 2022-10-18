""" Write a python script to print greater between two numbers. Print number only once
    even if the numbers are the same.
"""
num1=int(input("\nEnter first number: "))
num2=int(input("\nEnter second number: "))
if num1>num2:
    print('\n'f"{num1} is greater than {num2}.",end='\n\n')
elif num1<num2:
    print('\n'f"{num2} is greater than {num1}.",end='\n\n')
else:
    print('\n'f"{num1} both numbers are same.",end='\n\n')