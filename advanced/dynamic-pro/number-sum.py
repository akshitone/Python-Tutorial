from itertools import combinations


def check_sum(number, lst):
    sum_list = list()
    for comb_num in lst:
        if (comb_num[0]+comb_num[1]) == number:
            sum_list.append(comb_num)
    return sum_list


lst = [1, 2, 3, 7, 5, 8]
sum = 10
combination_list = list(combinations(lst, 2))
print(check_sum(sum, combination_list))
