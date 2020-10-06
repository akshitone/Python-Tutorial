ran = int(input("Enter number: "))
for num in range(1, ran):
    for i in range(2, num):
        if num % i == 0:
            break
    else:
        print(num)
