# Write a python script to print two given words in dictionary order.
print("\nEnter Two Words: ")
a,b=input(),input()
print((b,a) if a>b else (a,b))