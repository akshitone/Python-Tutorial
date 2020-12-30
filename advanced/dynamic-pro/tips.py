from collections import Counter

a = [1, 2, 3, 4, 3, 2, 3, 4, 6, 7, 5, 3, 2]
print(a)
max = max(set(a), key=a.count)
print(a)
print(max)


def sum(*a):
    lst = list(a)
    print(lst)


res = sum(3, 4, 6, 3, 2, 4, 5, 3)
