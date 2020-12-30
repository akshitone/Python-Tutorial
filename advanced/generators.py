def my_gen():
    yield 1
    yield 5
    yield 6
    yield 57


lst = list(my_gen())
print(lst)
