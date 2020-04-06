# 09/08/2019

def solution(input_list):
    n = len(input_list)
    n_sum = 0
    list_sum = 0
    for index in range(len(input_list)):
        list_sum += input_list[index]
        n_sum += (index + 1)

    return list_sum - (n_sum - n)


Input_list = [1, 2, 3, 4, 5, 5]
print(f'Input: {Input_list}')

result = solution(Input_list)
print(f'Ouput: {result}')
