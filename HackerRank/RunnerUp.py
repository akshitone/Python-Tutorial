arr = [5, 2, 3, 6, 6, 4]

max = max(arr)
cnt = arr.count(max)
print(sorted(arr)[-(cnt+1)])
