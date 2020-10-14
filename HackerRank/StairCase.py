n = 5
for i in range(1, n+1):
    print("#"*i)


lst = [1, 2, 3, 4, 5]

min_sum = sum(lst) - max(lst)
max_sum = sum(lst) - min(lst)

print(min_sum)
print(max_sum)
