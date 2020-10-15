lst = [1, 2, 3, 4, 5, 6]
n = 6
k = 5
cnt = 0
for i in range(n):
    for j in range(i, n):
        if (lst[i] + lst[j]) % k == 0 and i < j:
            print(lst[i], lst[j], k)
            cnt += 1

print(cnt)
