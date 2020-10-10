lst = list()
scoreList = list()
for _ in range(int(input())):
    name = input()
    score = float(input())
    lst.append([name, score])
    scoreList.append(score)

# mn = min(scoreList)
# print(scoreList)
# print(min(scoreList))
# print(lst)
# print(sec)
secondLowest = sorted(set(scoreList))[1]

for name, score in sorted(lst):
    if score == secondLowest:
        print(name)
