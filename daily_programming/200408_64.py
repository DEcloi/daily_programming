# 09/22/2019

def solution(input_list):
    count = 0
    max_count = 0
    max_index = -1
    prev_zero_index = -1
    for index in range(len(input_list)):
        if input_list[index] == 1:
            count += 1
        else:
            count = index - prev_zero_index
            prev_zero_index = index

        if count > max_count:
            max_count = count
            max_index = prev_zero_index

    return max_index


Input_list = [0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1]
print(f'Input: {Input_list}')

result = solution(Input_list)
print(f'Output: {result}')
