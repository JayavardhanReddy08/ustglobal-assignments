#Use filter() to extract all palindromic strings from a list.
l=['anil','malayalam','ganesh','raghu','taga']
l1=filter(lambda x:x==x[::-1],l)
print(list(l1))