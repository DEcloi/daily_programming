# 09/11/2019

def solution(input_list):
    front_index = 0
    back_index = len(input_list)
    for i in range(len(input_list)):
        if input_list[front_index] == 1:
            input_list.insert(back_index, 1)
            input_list.pop(front_index)
        elif input_list[front_index] == 2:
            input_list.insert(back_index, 2)
            input_list.pop(front_index)
            back_index -= 1
        else:
            front_index += 1


Input_list = [0, 1, 2, 2, 1, 0, 0, 2, 0, 1, 1, 0]
print(f'Input: {Input_list}')

solution(Input_list)
print(f'Output: {Input_list}')
