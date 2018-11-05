import numpy as np
import scipy.stats
from matplotlib import pyplot as plt


def factorial(n):
    if n == 0:
        return 1

    return n * factorial(n - 1)

print(factorial(0))
print(factorial(5))
print(factorial(6))

def factorial_tail(n, acc=1):
    if n == 0:
        return acc

    acc = n * acc
    return factorial_tail(n - 1, acc)


print("---tail----")
print(factorial_tail(0))
print(factorial_tail(5))
print(factorial_tail(6))


def factorial_iter(n):
    acc = 1

    for i in range(1, n + 1):
        acc *= i

    return acc


print("---iter---")
print(factorial_iter(0))
print(factorial_iter(5))
print(factorial_iter(6))


def factorial_iter_stack(n):
    stack = []
    result = 1

    while stack or n != 0:
        while n != 0:
            stack.append(n)
            n -= 1

        curr = stack.pop()
        result *= curr

    return result


print("---iter---")
print(factorial_iter_stack(0))
print(factorial_iter_stack(5))
print(factorial_iter_stack(6))
