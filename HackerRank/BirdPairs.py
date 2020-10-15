arr = [1, 4, 4, 4, 5, 3]

d = dict()
for i in arr:
    d[i] = d.get(i, 0) + 1

print(max(d, key=d.get))
# l = [0]*len(arr)
# print(l)
# for i in range(len(arr)):
#     l[arr[i]] += 1

# print(l)
# print(l.index(max(l)))
