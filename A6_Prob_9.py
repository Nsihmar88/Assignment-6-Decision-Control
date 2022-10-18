# Write a python script to check whether a given year is a leap year or not.
yr = int(input("\nEnter year in YYYY format: "))
if ((yr%4==0 and yr%100!=0) or (yr%400==0 )):
    print("\n"f"{yr} Leap Year.")
else:
    print("\n"f"{yr} Not a Leap Year.")