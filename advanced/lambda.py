from functools import reduce
def add10(x): return x+10


# add10 = lambda x:x+10
print(add10(10))

points2D = [(1, 2), (15, 1), (5, -1), (10, 4)]
points2D_sorted = sorted(points2D)
points2D_sorted_reverse = sorted(points2D, key=lambda x: x[1])
points2D_sorted_by_sum = sorted(points2D, key=lambda x: x[0]+x[1])

print(points2D)
print(points2D_sorted)
print(points2D_sorted_reverse)
print(points2D_sorted_by_sum)

num = [1, 2, 3, 4, 5]
num2 = map(lambda x: x*2, num)
# num2 = [x*2 for x in num2]
num2_even = filter(lambda x: x % 2 == 0, num)
num2_reduce = reduce(lambda x, y: x*y, num)
print(num)
print(list(num2))
print(list(num2_even))
print(num2_reduce)
