#Write a program to open a file and handle a FileNotFoundError.
try:
    f=open("data.text","r")
except FileNotFoundError:
    print("file not found")
else:
    print("successful")
finally:
    print("completed")