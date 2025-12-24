#Write a program using map() to calculate the length of each word in a list of strings.
l=['jaya','ram','anil','sunil','raja']
l1=map(lambda x:len(x),l)
print(list(l1))