# 29)How can you use list comprehension to generate a list of the first 10 Fibonacci numbers?
# Ans:-
def generate_fibonacci(n):
    fib_list = [0, 1]
    for i in range(2, n):
        fib_list.append(fib_list[i-1] + fib_list[i-2])
    return fib_list[:n]
first_ten_fib = generate_fibonacci(10)
print(first_ten_fib)
