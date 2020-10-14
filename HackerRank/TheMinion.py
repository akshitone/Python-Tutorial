s = 'BANANA'
stuart = list()
kevin = list()
for i in range(len(s)+1):
    for j in range(i):
        if s[j] in 'AEIOU':
            stuart.append(s[j:i])
        else:
            kevin.append(s[j:i])

# for i in range(len(s)):
#     if s[i] not in 'AEIOU':
#         vow = vow + len(s)-i
print(len(stuart))
print(len(kevin))
