# 10/09/2019

def solution(input_list):
    index = 0
    for _ in range(len(input_list)):
        if input_list[index] == 0:
            input_list.append(0)
            input_list.pop(index)
        else:
            index += 1


Input_list = [6, 0, 8, 2, 3, 0, 4, 0, 1]
print(f'Input: {Input_list}')

solution(Input_list)
print(f'Output: {Input_list}')
