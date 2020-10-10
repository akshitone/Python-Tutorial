for _ in range(int(input())):
    tpl = tuple(map(int, input().split()))
    print(hash(tpl))
