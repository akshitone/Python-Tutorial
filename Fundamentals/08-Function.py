# FUNCTIONS
'''
def whoAreYou():
    print("Hello, I'm Akshit Mithaiwala")


for i in range(5):
    whoAreYou()
'''


def add_sub(x, y):
    add = x + y
    sub = x - y
    return add, sub


addition, subtraction = add_sub(50, 20)
print(addition)
print(subtraction)

# UNDEFINE ARGUMENTS


def add(*b):
    sum = 0
    for i in b:
        sum += i
    print(b)
    return sum


result = add(5, 19, 54, 72)
print(result)

# **kwargs


def person(name, **kwargs):
    print("name:", name)
    print(kwargs)
    for key, value in kwargs.items():
        print(key, "-->", value)


person('Akshit Mithaiwala', age=22, mobile=7874987797, city='Surat')

# ODD-EVEN


def odd_even(li):
    even = []
    odd = []
    for i in li:
        if i % 2 == 0:
            odd.append(i)
        else:
            even.append(i)
    return odd, even


li = [5, 10, 15, 20, 25]
odd, even = odd_even(li)
print("odd numbers are:", odd)
print("even numbers are:", even)
