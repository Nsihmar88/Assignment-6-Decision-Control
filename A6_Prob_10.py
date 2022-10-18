# Write a python script to print greater among three numbers. Print number only once even if the numbers are the same.

num1=int(input("\nEnter first number: "))
num2=int(input("\nEnter second number: "))
num3=int(input("\nEnter third number: "))

if num1>num2 and num1>num3:
    print('\n'f"{num1} is greater.",end='\n\n')
elif num2>num3:
    print('\n'f"{num2} is greater.",end='\n\n')
elif num3>num1:
    print('\n'f"{num3} is greater.",end='\n\n')
else:
    print('\n'f"{num1} all numbers are same.",end='\n\n')