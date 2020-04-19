# 11/24/2019
import sys


def solution(input_list):
    def max_kadane():
        beg = 0
        start_index = 0
        end_index = 0
        max_value = -sys.maxsize - 1
        max_temp = -sys.maxsize - 1
        for index in range(len(input_list)):
            max_temp = max_temp + input_list[index]
            if input_list[index] > max_temp:
                max_temp = input_list[index]
                beg = index

            if max_temp > max_value:
                max_value = max_temp
                start_index = beg
                end_index = index

        return start_index, end_index

    def min_kadane():
        beg = 0
        start_index = 0
        end_index = 0
        max_value = -sys.maxsize - 1
        max_temp = -sys.maxsize - 1
        for index in range(len(input_list)):
            reverse_value = input_list[index] * -1
            max_temp = max_temp + reverse_value
            if reverse_value > max_temp:
                max_temp = reverse_value
                beg = index

            if max_temp > max_value:
                max_value = max_temp
                start_index = beg
                end_index = index

        return start_index, end_index

    start_index1, end_index1 = max_kadane()
    max1 = sum(input_list[start_index1:end_index1 + 1])

    start_index2, end_index2 = min_kadane()
    print(start_index2, end_index2)
    max2 = sum(input_list[0:start_index2]) + sum(input_list[end_index2 + 1:])

    print(max1, max2)
    if max1 > max2:
        return input_list[start_index1:end_index1 + 1], max1
    else:
        return input_list[end_index2 + 1:] + input_list[0:start_index2], max2


Input_list1 = [2, 1, -5, 4, -3, 1, -3, 4, -1]
Input_list2 = [8, -7, -3, 5, 6, -2, 3, -4, 2]
Input_list3 = [-3, 1, -3, 4, -1, 2, 1, -5, 4]
print(f'Input: {Input_list2}')

result_list, result = solution(Input_list2)
print(f'Output: {result_list}, {result}')
