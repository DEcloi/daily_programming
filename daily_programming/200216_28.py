def solution(input_list):
    result = 1
    count = 1
    for i in input_list:
        if i > result:
            return result
        result += count
        count += 1

    return None


Input_list = [1, 2, 3, 8]
print(f'Input: {Input_list}')

result = solution(Input_list)
print(f'Output: {result}')
