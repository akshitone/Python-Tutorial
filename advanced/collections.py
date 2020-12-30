from collections import Counter

lst = [10, 20, 30, 10, 20, 40, 50, 10, 30, 40, 10, 20, 20, 20]

counter = Counter(lst)

print(counter.most_common())
