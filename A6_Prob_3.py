# Write a python script to check whether a given number is even or odd.
num=int(input("\nEnter a number to check entred number is even or odd: "))
if num%2==0:
    print('\n'f"{num} is Even Number.",end='\n\n')
else:
    print('\n'f"{num} is Odd Number.",end='\n\n')