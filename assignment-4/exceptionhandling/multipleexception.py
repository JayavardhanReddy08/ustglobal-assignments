#Write a program to handle multiple exceptions in a single try block.
try:
    n=[10,30,50,20,40]
    ind=int(input())
    d=int(input())
    result=n[ind]/d 
except ZeroDivisionError:
    print("denominator not allow zero")
except ValueError:
    print("type int val")
except IndexError:
    print("exceed")
else:
    print(result)
finally:
    print("ok")                    