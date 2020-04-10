# 10/23/2019


def solution(input_list):
    result = 0
    max_value = input_list[-1]
    for value in reversed(input_list[:-1]):
        if value > max_value:
            max_value = value
        else:
            result = max(result, max_value - value)

    return result


Input_list = [3, 7, 9, 5, 1, 3, 5, 8]
print(f'Input: {Input_list}')

result = solution(Input_list)
print(f'Output: {result}')
