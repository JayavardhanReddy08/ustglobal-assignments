#Write a program using filter() to find numbers greater than 50 from a list.
l=[10,20,30,40,50,70,90,101]
l1=filter(lambda x:x>50,l)
print(list(l1))