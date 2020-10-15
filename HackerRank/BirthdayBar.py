n = 5
lst = [4]
d = 4
m = 1
i = 0
cnt = 0
for i in range(len(lst)):
    sum = 0
    for j in range(i, m+i):
        if j < len(lst):
            sum += lst[j]
    if sum == d:
        cnt += 1
print(cnt)

# sum = 0
# while(i < len(lst)):
#     for j in range(m):
#         sum += lst[i]
#         print(i, sum)
#     sum = 0
#     i += 1
