# 18)Write a Python function that takes a dictionary and returns a list of keys that have values greater than 50.
# Ans:-
def dictionary(d):
    for I in d.keys():
           if d[I]>50:
               print(I)
D={'a':50,'b':10,'c':100,'d':20,'e':50}
dictionary(D)
