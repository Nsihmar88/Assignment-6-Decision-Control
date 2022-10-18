# Write a python script to check whether a given number is positive, negative or zero.
num=int(input("\nEnter a number to check entred number is positive, negative or zero: "))
if num>0:
    print('\n'f"{num} is Postive Number .",end='\n\n')
elif num<0:
    print('\n'f"{num} is Negative Number.",end='\n\n')
else:
    print('\n'"Zero.",end='\n\n')