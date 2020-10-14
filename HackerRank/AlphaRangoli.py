n = 3

lst = list(map(chr, range(97, 123)))
x = lst[n-1::-1]+lst[1:n]
m = len('-'.join(x))
for j in range(1, n):
    print('-'.join(lst[n-1:n-j:-1]+lst[n-j:n]).center(m, '-'))
for i in range(n, 0, -1):
    print('-'.join(lst[n-1:n-i:-1]+lst[n-i:n]).center(m, '-'))
