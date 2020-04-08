# 09/29/2019


def solution(input_list):
    for index in range(len(input_list) - 1):
        if index % 2 == 0:
            if input_list[index] > input_list[index + 1]:
                input_list[index], input_list[index + 1] = input_list[index + 1], input_list[index]
        else:
            if input_list[index + 1] > input_list[index]:
                input_list[index], input_list[index + 1] = input_list[index + 1], input_list[index]


Input_list1 = [1, 2, 3, 4, 5, 6, 7]
Input_list2 = [9, 6, 8, 3, 7]
Input_list3 = [6, 9, 2, 5, 1, 4]
print(f'Input: {Input_list3}')

solution(Input_list3)
print(f'Output: {Input_list3}')
