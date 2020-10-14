grades = [73, 67, 38, 33]
newScore = []
for i in grades:
    rem = i % 5
    if rem > 2:
        latestScore = i + (5-rem)
        if latestScore < 40:
            newScore.append(i)
        else:
            newScore.append(latestScore)
    else:
        newScore.append(i)

print(newScore)
