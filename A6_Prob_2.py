# Write a python script to check whether a given number is divisible by 5 or not.
num=int(input("\nEnter a number to check entred number is divisible by 5 or not: "))
if num%5==0:
    print('\n'f"{num} is divisible by 5.",end='\n\n')
else:
    print('\n'f"{num} is not divisible by 5.",end='\n\n')