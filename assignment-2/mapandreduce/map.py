# 21)How does the map() function work in Python? Give an example where you square each number in a list.
# Ans:- 
# Map function returns an iterato and will not process elements until you ask it to.
# Turn it into a list to force all elements to be processed:
L=[1,2,3,4,5]
L2=map(lambda x:x**2 ,L)
print(list(L2))

