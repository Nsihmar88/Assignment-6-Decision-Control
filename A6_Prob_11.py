# Write a python script to take the month value in numeric format and display the number of days in it.
month=int(input("Enter month number: "))

if month in (1,3,5,7,8,10,12):
    print("\n"f"Number of days are 31 in month {month}.")
elif month in(4,6,9,11):
    print("\n"f"Number of days are 30 in month {month}.")
elif (month==2):
    print("\n"f"Number of days are 28 or 29 in month {month}.")
else:
    print("\n"f"Invalid month {month}.")