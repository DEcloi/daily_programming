# 08/28/2019

def solution(input_list):
    sum = 0
    result = list()
    for i in range(len(input_list)):
        sum += input_list[i]
        for j in range(i+1, len(input_list)):
            sum += input_list[j]
            if sum == 0:
                result.append(input_list[i: j+1])

        sum = 0

    return result

Input_list = [3, 4, -7, 3, 1, 3, 1, -4, -2, -2]
print(f'Input: {Input_list}')

result = solution(Input_list)
if result is not None:
    print(f'Output: 부분 배열 존재')
    for i in result:
        print(f'{i}')
else:
    print(f'Output: 부분 배열 존재하지 않음')
