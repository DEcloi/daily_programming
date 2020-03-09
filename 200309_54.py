def solution(input_list, s):
    max_len = 0
    sum_list = {}
    for i in range(len(input_list)):
        sum_num = sum(input_list[:i+1])
        if sum_num not in sum_list:
            sum_list[sum_num] = i

        if sum_num - s in sum_list and max_len < i - sum_list[sum_num - s]:
            max_len = i - sum_list[sum_num - s]
            ending_index = i

    print(f'Output: {input_list[ending_index - max_len + 1: ending_index + 1]}')


Input_list = [5, 6, -5, 5, 3, 5, 3, -2, 0]
S = 8
print(f'Input: {Input_list}, S: {S}')

solution(Input_list, S)
