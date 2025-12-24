#Write a Python program using map() to convert a list of integers into their squares.
l=[1,2,3,4,5,6,7,8,9]
l1=map(lambda x:x**2 ,l)
print(list(l1))