lst = ['d', 'd', 'u', 'u', 'd', 'd', 'u', 'd', 'u', 'u', 'u', 'd']
vally = 0
cnt = 0
for i in lst:
    if i == 'u':
        cnt = cnt + 1
        if cnt == 0:
            vally = vally + 1
    else:
        cnt = cnt - 1

print(vally)
