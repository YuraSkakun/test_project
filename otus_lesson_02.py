def fib(n):
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a + b
    return result

print(fib(100))


def recur_fib(n):
    if n <= 1:
        return n
    return recur_fib(n - 1) + recur_fib(n - 2)

print(recur_fib(10))
