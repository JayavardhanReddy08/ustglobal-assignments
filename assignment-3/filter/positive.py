#Given a list of integers, use filter() to remove all negative numbers.
numbers = [10, -5, 3, -2, 0, 7, -8, 4]
positive_numbers = list(filter(lambda x: x >= 0, numbers))
print(positive_numbers)