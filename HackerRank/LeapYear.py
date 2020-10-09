def is_leap(year):
    leap = False

    if year % 4 == 0 and (year % 400 == 0 or year % 100 != 0):
        leap = True

    return leap


year = int(input())
print(is_leap(year))

for i in range(1, 5+1):
    print(i, end="")
