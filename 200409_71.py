# 10/16/2019


def solution(input_list):
    left = [1]
    right = [1]

    for index in range(len(input_list) - 1):
        left.append(left[index] * input_list[index])

    for index in range(len(input_list) - 1, 0, -1):
        right.insert(0, right[0] * input_list[index])

    for index in range(len(input_list)):
        input_list[index] = left[index] * right[index]


Input_list1 = [1, 2, 3, 4, 5]
Input_list2 = [5, 3, 4, 2, 6, 8]
print(f'Input: {Input_list2}')

solution(Input_list2)
print(f'Output: {Input_list2}')
