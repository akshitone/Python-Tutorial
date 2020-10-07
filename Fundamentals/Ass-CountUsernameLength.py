def count(users):
    resUser = []
    count = 0
    for user in users:
        if len(user) > 5:
            count += 1
            resUser.append(user)
    return resUser, count


users = ['akshit', 'suru', 'viral', 'rajan', 'ashwini']
res, cnt = count(users)
print(res, cnt)
