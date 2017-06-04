# Fibonacci numbers module


def fib_gen(n):    # write Fibonacci series up to n
    a, b = 0, 1
    while b < n:
        yield b
        a, b = b, a + b


def fib_list(n):   # return Fibonacci series up to n
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a + b
    return result
