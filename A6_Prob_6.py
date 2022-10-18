# Write a python script to check whether a given number is a three digit number or not.

num=int(input("\nEnter a number: "))

if (num>99 and num<=999):
    print('\n'f"{num} is three digit number.",end='\n\n')
else:
    print('\n'f"{num} is not three digit number.",end='\n\n')