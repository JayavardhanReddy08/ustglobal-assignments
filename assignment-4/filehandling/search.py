word = input("Enter word to search: ")
f = open("write1.txt","r")
line_no = 1
for line in f:
    if word in line:
        print("Word found at line number:", line_no)
    line_no += 1
f.close()
