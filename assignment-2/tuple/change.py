# 9) Given the tuple t = (1, 2, 3, 4), how can you change the value 3 to 100?
# Ans:-First convert tuple to list and modify element and then convert to tuple.
T=(1,2,3,4)
L=list(T)
L[2]=100
T1=tuple(L)
print(T1)        #(1,2,100,4)
