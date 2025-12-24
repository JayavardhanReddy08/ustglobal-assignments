#Given a list of temperatures in Celsius, use map() to convert them to Fahrenheit.
l=[35,45,23,11,25,29,35,30,37]
l1=map(lambda x:(x*9/5)+32,l)
print(list(l1))
