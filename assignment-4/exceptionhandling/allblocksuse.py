#Write a Python program that uses try, except, else, and finally blocks.
try:
    a=input("first name send")
    b=input("second name fill")
    result=a+b
except ValueError:
     print("enter string")
except TypeError:
     print("not cancatinate string and int")
else:
     print(result)
finally:
     print("success") 