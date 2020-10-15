k1 = 0
m1 = 3
k2 = 4
m2 = 2
i = 0
for i in range(1, 10):
    kan1 = k1 + (m1*i)
    kan2 = k2 + (m2*i)
    if (kan1 == kan2):
        print("YES")
    else:
        print("NO")

# if v1 > v2:
#         if (x1-x2)%(v2-v1) == 0:
#             return("YES")
#         else:
#             return("NO")
#     else:
#         return("NO")
