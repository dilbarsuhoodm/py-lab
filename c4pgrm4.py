def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def print_fibonacci_series(count):
    for i in range(count):
        print(fibonacci(i), end=' ')

num_terms = 10
print_fibonacci_series(num_terms)

