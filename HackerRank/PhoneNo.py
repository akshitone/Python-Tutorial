# Enter your code here. Read input from STDIN. Print output to STDOUT
'''
lst = list()
n = int(input())
for _ in range(n):
    line = input().split()
    name, number = line[0], line[1]
    lst.append([name, number])

output = list()
for i in range(n):
    line = input()
    name = lst[i][0]
    if line == name:
        output.append(lst[i])
        # print(f"{name}={lst[i][1]}")
    else:
        output.append('Not found')
        # print('Not found')

print(lst)
print(output)
for i in range(n):
    if lst[i][1] == '':
        print(f"{lst[i][0]}={lst[i][1]}")
    else:
        print(lst[i])
'''

n = int(input())

phone_book = dict()

for i in range(n):
    line = input().split()
    phone_book[line[0]] = line[1]

print(phone_book)
name = input()
while name:
    phone_number = phone_book.get(name)
    if phone_number:
        print(name + '=' + phone_number)
    else:
        print('Not found')
    name = input()
