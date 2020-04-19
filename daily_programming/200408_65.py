# 09/25/2019
import sys


def solution(input_list):
    min1, min2 = input_list[0], sys.maxsize
    max1, max2 = input_list[0], -sys.maxsize - 1
    for value in input_list[1:]:
        if min1 > value:
            min2 = min1
            min1 = value
        elif min2 > value:
            min2 = value

        if value > max1:
            max2 = max1
            max1 = value
        elif value > max2:
            max2 = value

    if (max1 * max2) > (min1 * min2):
        return max1, max2
    else:
        return min1, min2


Input_list = [-10, -3, 9, 5, 6, -2]
print(f'Input: {Input_list}')

max1, max2 = solution(Input_list)
print(f'Output: [{max1}, {max2}]')
