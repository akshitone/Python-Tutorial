n = int(input())


# def fibo(n):
#     if n <= 2:
#         return 1
#     return fibo(n-1) + fibo(n-2)


# print(fibo(n))


a, b = 1, 1
for i in range(n):
    if i == n-1:
        print(a)
    sum = a+b
    a = b
    b = sum
