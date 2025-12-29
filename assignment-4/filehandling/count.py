#Write a Python program to count the number of lines, words, and characters in a text file.
f=open("write1.txt","r")
l=0
w=0
c=0
for lines in f:
    l=l+1
    for words in lines:
        w=w+1 
        for character in words:
            c=c+1
print(l)
print(w)
print(c)