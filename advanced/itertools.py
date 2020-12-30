from itertools import product, permutations, combinations, combinations_with_replacement, accumulate, groupby

# two list possible combination
a = [1, 2]
b = [3, 4]
prod = product(a, b)
# prod = product(a, b, repeat=2)
print(list(prod))

num = [1, 2, 3, 4, 5]

# all combination
perm = permutations(num, 2)
print(list(perm))

# all unique possible combination
comb = combinations(num, 2)
print(list(comb))

# it consider (1,1) (2,2) (3,3)
comb_with_replace = combinations_with_replacement(num, 2)
print(list(comb_with_replace))

acc = accumulate(num)
print(num)
print(list(acc))

num_MAX = [1, 2, 7, 3, 4, 5]
acc_max = accumulate(num_MAX, func=max)
print(list(acc_max))

# new = []
# sum = 0
# for i in num:
#     sum += i
#     new.append(sum)

# print(new)


def odd_even_num(num):
    return num < 5


odd_even = [1, 2, 3, 4, 5, 6, 7, 8]
grp = groupby(odd_even, key=odd_even_num)
for key, value in grp:
    print(key, list(value))

persons = [
    {'name': 'akshit', 'age': 21},
    {'name': 'viral', 'age': 21},
    {'name': 'suru', 'age': 22},
    {'name': 'rajan', 'age': 23},
]
grp_person = groupby(persons, key=lambda per: per['age'])
for key, value in grp_person:
    print(key, list(value))
