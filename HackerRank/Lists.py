lst = list()
# line = input().split()
# action, numbers = line[0], list(map(int, line[1:]))
# lst.insert(numbers[0], numbers[1])
# print(lst)

for _ in range(int(input())):
    line = input().split()
    action, numbers = line[0], list(map(int, line[1:]))
    if action == 'append':
        lst.append(numbers[0])
    if action == 'insert':
        lst.insert(numbers[0], numbers[1])
    if action == 'remove':
        lst.remove(numbers[0])
    if action == 'sort':
        lst.sort()
    if action == 'print':
        print(lst)
    if action == 'pop':
        lst.pop()
    if action == 'reverse':
        lst.reverse()
