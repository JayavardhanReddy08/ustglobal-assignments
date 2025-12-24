# 5) Write a Python function that removes duplicates from a list without using the set() function.
def duplicate(l):
    L1=l 
    L2=[]
    for I in L1:
        if I not in L2:
            L2.append(I)
    print(L2)
L=[1,2,3,4,5,5,5,5]
duplicate(L)
