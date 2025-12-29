#Write a program that accepts user input and handles a ValueError if the input is not an integer.
try:
    a=int(input())
except ValueError:
    print("enter integer value")
else:
    print("successful")
finally:
    print("done")    