#Write a program to copy the contents of one text file into another file.
f=open("write1.txt","r")
d=f.read()
f.close()
f1=open("write2.txt","w+")
f1.write(d)
f1.seek(0)
print(f1.read())
f1.close()