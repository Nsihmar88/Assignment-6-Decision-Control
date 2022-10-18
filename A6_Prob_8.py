""" Write a python script to check whether a given quadratic equation has 
    two real & distinct roots, real & equal roots or imaginary roots.
"""
a=int(input("\nEnter Value of a: "))
b =int(input("\nEnter Value of b: "))
c =int(input("\nEnter Value of c: "))

d=(b*b)-(4*a*c)
if d > 0: 
    print("\nThe equation has two real and distinct roots.")
elif d < 0:
    print("\nThe equation has two complex roots.")
elif d == 0:
    print("\nThe equation has only one real root.")
