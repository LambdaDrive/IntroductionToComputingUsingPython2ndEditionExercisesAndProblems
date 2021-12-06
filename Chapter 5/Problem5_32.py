def fib(n):
    first = 0
    second = 1
    third = 1
    for i in range(n):
        third = first + second
        first, second = second, third
    return second
