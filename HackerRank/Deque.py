from collections import deque

d = deque()
d.append('1')
d.append('2')
d.append('23')
d.extend('23')
d.extend('3456')
d.pop()
d.remove('2')
print(d)

d.reverse()
print(d)

d.rotate()
print(d)


n = int(input())
lst = []
for i in range(n):
    val = input()
    lst.append(val)

print(lst)

for i in lst:
    print(i)
