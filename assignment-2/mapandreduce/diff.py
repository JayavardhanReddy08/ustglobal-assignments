# 25)Compare and contrast the map() and filter() functions in Python.
# Ans:-
# 1)Higher-order functions: Both filter() and map() are higher-order functions; they accept another function (or a lambda function) and an iterable (like a list, tuple, or string) assignment
# 2)Lazy evaluation: In Python 3, both functions return iterators, meaning they perform their operations lazily (processing items one by one as needed) rather than creating an entirely new list in memory immediately 
# 3)Element-wise operation: Each item in the input iterable is processed individually and sequentially