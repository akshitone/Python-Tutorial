# ANONYMOUS FUNCTION - LAMBDA
from functools import reduce


def sqr(s): return s*s
def add(a, b): return a+b, a-b


res = sqr(10)
add, sub = add(10, 20)
print(res)
print(add)
print(sub)


# ODD - EVEN
numbers = [4, 5, 2, 7, 9, 8, 1]
even = list(filter(lambda number: number % 2 == 0, numbers))
odd = list(map(lambda number: sqr(number), numbers))
sum = reduce(lambda a, b: a+b, numbers)
print(even)
print(odd)
print(sum)
print(__name__)
