#Write a Python program using filter() to extract all even numbers from a list.

l=[1,2,3,4,5,6,7,8,9]
l1=filter(lambda x:x%2==0,l)
print(list(l1))