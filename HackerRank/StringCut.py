string = 'AABACACAA'
k = 3
cnt = 0
s = ''
for i in string:
    if i not in s:
        s = s + i
    cnt += 1
    if cnt == k:
        print(s)
        s = ''
        cnt = 0
