s = 'aba'
n = 10
rem = n % len(s)
eq = n // len(s)
sub_s = s*eq + s[:rem]
print(sub_s)
cnt = 0
for i in sub_s:
    if i == 'a':
        cnt += 1

a = sub_s.count('a')
print(cnt)
print(a)

# rem = n % len(s)
# eq = n // len(s)
# c = s.count('a')
# cnt1 = eq*c
# cnt2 = s[:rem].count('a')

# print(cnt1 + cnt2)
