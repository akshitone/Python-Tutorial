'''
n = 9
scores = [3, 4, 21, 36, 10, 28, 35, 5, 24, 42]
lst = []

min_cnt = 0
max_cnt = 0
for i in range(n+1):
    lst.append(scores[i])
    max_score = max(lst)
    min_score = min(lst)
    print(min_score, max_score, lst)
    if i == 0:
        pass
    elif scores[i] == min_score:
        # print(scores[i], min_score)
        min_cnt += 1
    elif scores[i] == max_score:
        # print(scores[i], max_score)
        max_cnt += 1

print(max_cnt, min_cnt)
'''

n = 10
scores = [3, 4, 21, 36, 10, 28, 35, 5, 24, 42]
max_score = 0
min_score = 0
max_count = 0
min_count = 0
for i in range(n):
    print(i, min_score, max_score)
    if i == 0:
        min_score = scores[i]
        max_score = scores[i]
    elif scores[i] > max_score:
        max_score = scores[i]
        max_count += 1
    elif scores[i] < min_score:
        min_score = scores[i]
        min_count += 1

print(max_count, min_count)
