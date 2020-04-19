def solution(input_list):
    input_dict = {}
    for data in input_list:
        try:
            input_dict[data] += 1
        except:
            input_dict[data] = 1

    result = []
    for item in input_dict:
        if input_dict[item] > 1:
            result.append(item)

    return result


Input_list = [5, 4, 3, 2, 1, 1, 0, 0, 1, 2, 4]
print(f'Input: {Input_list}')

result = solution(Input_list)
print(f'Output: {result}')
