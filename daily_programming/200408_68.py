# 10/06/2019


def solution(input_list):
    input_dict = dict()
    for item in input_list:
        if item not in input_dict.keys():
            input_dict[item] = 1
        else:
            input_dict[item] += 1

    for key, item in input_dict.items():
        if item > (len(input_list) // 2):
            return key

    return None


def majority_Element(input_list):
    counter = 1
    major = input_list[0]
    for i in input_list[1:]:
        if major != i and counter != 0:
            counter -= 1
        elif major != i and counter == 0:
            major = i
            counter += 1
        else:
            counter += 1

    counter = 0
    for i in input_list:
        if i == major:
            counter += 1
        if counter > (len(input_list) // 2):
            return major

    return None


Input_list = [2, 8, 7, 2, 2, 5, 2, 3, 1, 2, 2, 2, 2, 2, 2, 1, 9, 10, 11]
print(f'Input: {Input_list}')

result = solution(Input_list)
print(f'Output: {result}')

result2 = majority_Element(Input_list)
print(f'Output: {result2}')
