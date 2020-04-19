# 10/20/2019


def solution(input_list):
    n = len(input_list)
    index = 0
    end_index = 0
    max_len = 0
    while index + 1 < n:
        temp_len = 1
        while index + 1 < n and input_list[index] < input_list[index + 1]:
            index += 1
            temp_len += 1

        while index + 1 < n and input_list[index] > input_list[index + 1]:
            index += 1
            temp_len += 1

        if temp_len > max_len:
            max_len = temp_len
            end_index = index

    return input_list[end_index - max_len + 1: end_index + 1]


Input_list1 = [3, 5, 8, 4, 5, 9, 10, 8, 5, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
Input_list2 = [1, 2, 3, 4, 5]
Input_list3 = [5, 4, 3, 2, 1]
print(f'Input: {Input_list1}')

result = solution(Input_list1)
print(f'Output: {result}')
