# 08/25/2019

def solution(input_list, s):
    result = ""
    for i in range(len(input_list)):
        find_value = s - input_list[i]
        if find_value in input_list[i:]:
            index1 = i
            index2 = input_list.index(find_value)
            if index1 != index2:
                result += f'({index1}, {index2}) '

    return result

Input_list = [8, 7, 2, 5, 3, 1]
S = 10

print(f'Input: 정수 배열 =  {Input_list}, S = {S}')

result = solution(Input_list, S)
print(f'Output: {result}')
