# FIBONACCI NUMBER
'''
def fibo(n):
    a = 0
    b = 1
    c = 0
    if n == 1:
        print(a)
    elif n < 0:
        print("invalid number")
    else:
        print(a)
        print(b)
        for i in range(2, n):
            c = a + b
            a = b
            b = c
            print(c)


n = int(input("Enter number: "))
fibo(n)
'''

# FIBONACCI UP TO CERTAIN NUMBER


def fiboNumber(n):
    a = 0
    b = 1
    c = 0
    if n < 0:
        print("invalid number")
    else:
        print(a)
        print(b)
        c = a + b
        while(c <= n):
            print(c)
            a = b
            b = c
            c = a + b


n = int(input("Enter number: "))
fiboNumber(n)
