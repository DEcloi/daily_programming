# 08/21/2019

def solution(input_list):
    sum = 0
    max_len = 0
    input_dict = {}
    for index in range(len(input_list)):
        if input_list[index] == 0:
            sum -= 1
        else:
            sum += 1

        if sum in input_dict.keys():
            temp_start_index = input_dict[sum] + 1
            temp_end_index = index
            if temp_end_index - temp_start_index > max_len:
                start_index = temp_start_index
                end_index = temp_end_index
                max_len = end_index - start_index
        else:
            input_dict[sum] = index

    return input_list[start_index:end_index+1]


Input_list1 = [0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0]
Input_list2 = [0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1, 1]
Input_list3 = [1, 1, 1, 1, 1, 0, 0]
print(f'Input: {Input_list1}')

result = solution(Input_list1)
print(f'Output: {result}')
