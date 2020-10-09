def convertNumberString(lst):
    for i in lst:
        if i.isnumeric():
            num = i
            for i in range(3):
                print(num, end='')
            print()
        else:
            print(i, '#')


lst = ['41', 'DROND', 'GIRIRAJ', '13', 'ZARA']
convertNumberString(lst)


def Reverse(lst):
    new_lst = lst[::-1]
    return new_lst


n = int(input("enter range:"))
lst = []
for i in range(n):
    val = int(input())
    lst.append(val)
print(lst)

print(Reverse(lst))
