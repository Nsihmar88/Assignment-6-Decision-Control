""" Write a python script to accept one complex number from the user and 
    display the greater number between real part and imaginary part.
"""
num=complex(input("enter a complex number: "))
if num.real>num.imag:
    print(num.real)
else:
    print(num.imag)