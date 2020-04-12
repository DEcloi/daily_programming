# 11/10/2019
import copy


def solution(input_list):
    n = len(input_list)
    inc_list = [[] for _ in range(len(input_list))]
    dec_list = [[] for _ in range(len(input_list))]

    inc_list[0] = [input_list[0]]
    for i in range(1, n):
        for j in range(i):
            if input_list[i] > input_list[j] and len(inc_list[j]) > len(inc_list[i]):
                inc_list[i] = copy.deepcopy(inc_list[j])

        inc_list[i].append(input_list[i])

    dec_list[n - 1] = [input_list[-1]]
    for i in range(n - 2, -1, -1):
        for j in range(n - 1, i - 1, -1):
            if input_list[i] > input_list[j] and len(dec_list[j]) > len(dec_list[i]):
                dec_list[i] = copy.deepcopy(dec_list[j])

        dec_list[i].insert(0, input_list[i])

    max_len = 0
    result_list = list()
    for index in range(n):
        temp_list = inc_list[index] + dec_list[index][1:]
        if len(temp_list) > max_len:
            max_len = len(temp_list)
            result_list = temp_list

    return result_list


Input_list1 = [4, 2, 5, 9, 7, 6, 10, 3, 1]
Input_list2 = [1, 2, 3, 4, 5]
Input_list3 = [5, 4, 3, 2, 1, 2, 3, 2]
print(f'Input: {Input_list1}')

result = solution(Input_list1)
print(f'Output: {result}')
