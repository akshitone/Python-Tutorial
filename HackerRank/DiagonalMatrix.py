lst = [[11, 2, 4], [4, 5, 6], [10, 8, -12]]
sum1 = 0
sum2 = 0
for i in range(len(lst)):
    cnt = i
    k = (len(lst)-1) - i
    for j in range(len(lst)):
        if i == j:
            sum1 += lst[i][j]
        if i == cnt and j == k:
            sum2 += lst[i][j]

print(sum1)
print(sum2)
print(abs(sum1-sum2))
