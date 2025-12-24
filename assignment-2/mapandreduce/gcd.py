# 24)Write a Python program that uses reduce() to find the greatest common divisor (GCD)of a list of numbers.
# Ans:- 
from functools import reduce
import math
def find_list_gcd(numbers):
    list_gcd = reduce(math.gcd, numbers)
    return list_gcd
data = [12, 18, 30, 48]
print(find_list_gcd(data))
