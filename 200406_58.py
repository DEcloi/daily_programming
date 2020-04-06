# 09/01/2019

def solution(input_list):
    sum = 0
    result = list()
    for i in range(len(input_list)):
        if input_list[i] == 0:
            result.append(input_list[i])
        else:
            sum += input_list[i]
            for j in range(i+1, len(input_list)):
                sum += input_list[j]
                if sum == 0:
                    result.append(input_list[i: j+1])
        sum = 0

    return result


Input_list1 = [4, 2, -3, -1, 0, 4]
Input_list2 = [3, 4, -7, 3, 1, 3, 1, -4, -2, -2]

print(f'Input: {Input_list1}')

result = solution(Input_list1)
if result is not None:
    print(f'Output:')
    for i in result:
        print(f'{i}')
else:
    print(f'Output:')
