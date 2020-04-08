# 10/02/2019


def solution(input_list):
    results = list()
    left = 0
    right = sum(input_list)
    for index in range(len(input_list)):
        right -= input_list[index]
        if left == right:
            results.append(index)
        left += input_list[index]

    return results


Input_list = [0, -3, 5, -4, -2, 3, 1, 0]
print(f'Input: {Input_list}')

result = solution(Input_list)
print(f'Output: {result}')
