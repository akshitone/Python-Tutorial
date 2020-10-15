s = 7
t = 11
a = 5
b = 15
m = 3
n = 2
apples = [-2, 2, 1]
oranges = [5, -6]
app_cnt = 0
ora_cnt = 0
for i in apples:
    app_dis = i + a
    if app_dis in range(s, t+1):
        app_cnt += 1
for i in oranges:
    ora_dis = i + b
    if ora_dis in range(s, t+1):
        ora_cnt += 1

print(app_cnt, ora_cnt)
