lst = [-4, 3, -9, 0, 4, 1]
zes = 0
pos = 0
nes = 0
ln = len(lst)
for i in lst:
    if i == 0:
        zes += 1
    elif i < 0:
        nes += 1
    else:
        pos += 1

print(pos/ln)
print(nes/ln)
print(zes/ln)
