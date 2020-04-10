# 10/27/2019
import sys


def solution(input_list):
    max_value = -sys.maxsize - 1
    max_temp = -sys.maxsize - 1
    for i in input_list:
        max_temp = max_temp + i
        max_temp = max(max_temp, i)
        max_value = max(max_temp, max_value)

    return max_value


Input_list1 = [-2, 1, -3, 4, -1, 2, 1, -5, -4]
Input_list2 = [-8, -3, -6, -2, -5, -4]
print(f'Input: {Input_list1}')

result = solution(Input_list1)
print(f'Output: {result}')
