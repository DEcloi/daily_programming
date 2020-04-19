# 12/01/2019


def solution(input_list):
    result_list = list()
    min_num = input_list[0]
    max_num = input_list[0]
    for index in range(1, len(input_list)):
        if input_list[index] > max_num:
            max_num = input_list[index]
        elif max_num > min_num:
            result_list.append([min_num, max_num])
            min_num = input_list[index]
            max_num = input_list[index]

    if max_num > min_num:
        result_list.append([min_num, max_num])

    return result_list


Input_list1 = [1, 5, 2, 3, 7, 6, 4, 5]
Input_list2 = [10, 8, 6, 5, 4, 2]
Input_list3 = [1, 9, 2, 3, 6, 5, 4, 3, 7, 10, 9]
print(f'Input: {Input_list3}')

result = solution(Input_list3)
print(f'Output: {result}')
