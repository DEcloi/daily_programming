# 11/27/2019
import sys
import numpy as np


def solution(input_np, k):
    max_sum = -sys.maxsize - 1
    max_list = list()
    m = len(input_np[0])
    n = len(input_np)
    for x in range(m - (k - 1)):
        for y in range(n - (k - 1)):
            x_slice = slice(x, x+k)
            y_slice = slice(y, y+k)
            cur_sum = sum(sum(input_np[x_slice, y_slice]))
            if cur_sum > max_sum:
                max_sum = cur_sum
                max_list = input_np[x_slice, y_slice]

    return max_list


Input_list = np.array([[3, -4, 6, -5, 1],
                       [1, -2, 8, -4, -2],
                       [3, -8, 9, 3, 1],
                       [-7, 3, 4, 2, 7],
                       [-3, 7, -5, 7, -6]])
K = 2
print(f'Input: mat = {Input_list}')
print(f'k = {K}')

result = solution(Input_list, K)
print(f'Output: {result}')
