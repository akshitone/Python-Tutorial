num = int(input())
line = list(input().split())
print(line)

count = 0
cnt = 0
upside = [9, 6]
for no in range(num):
    for i in line[no]:
        if i == '9' or i == '6':
            count += 1
    if count > 1:
        count += 1
        cnt = cnt + count

print(count)
