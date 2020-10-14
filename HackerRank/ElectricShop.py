line = input().split()
print(line)
budget, k_part, u_part = int(line[0]), int(line[1]), int(line[2])
k_price = list()
u_price = list()

for _ in range(k_part):
    val = int(input())
    k_price.append(val)

for _ in range(u_part):
    val = int(input())
    u_price.append(val)

maxamount = -1
for i in k_price:
    for j in u_price:
        if i+j <= budget:
            print(maxamount)
            maxamount = max(maxamount, i+j)

print("----------", maxamount)
