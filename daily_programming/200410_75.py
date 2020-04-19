# 10/30/2019
import sys


def solution(input_list):
    start_index = 0
    end_index = 0
    max_value = -sys.maxsize - 1
    max_temp = -sys.maxsize - 1
    for index in range(len(input_list)):
        max_temp = max_temp + input_list[index]
        if input_list[index] > max_temp:
            max_temp = input_list[index]
            start_index = index
        if max_temp > max_value:
            max_value = max_temp
            end_index = index

    return input_list[start_index:end_index+1]


Input_list1 = [-2, 1, -3, 4, -1, 2, 1, -5, -4]
Input_list2 = [8, -7, -3, 5, 6, -2, 3, -4, 2]
print(f'Input: {Input_list2}')

result = solution(Input_list2)
print(f'Output: {result}')
