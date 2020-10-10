n = 9
ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]

cnt = 0
d = dict()
for i in ar:
    d[i] = d.get(i, 0) + 1

for i in d.keys():
    cnt += d[i]//2
print(d)
print(cnt)
# print(n)
# print(ar)

# cnt = 0
# for i in ar:
#     val = i
#     print(val)
#     for j in ar:
#         print("j===", j)
#         if val == j:
#             ar.remove(val)
#             if j:
#                 ar.remove(j)
#             else:
#                 cnt = cnt + 1

# print(ar)
# print(cnt)
