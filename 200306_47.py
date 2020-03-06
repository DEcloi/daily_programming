def solution(input_list):
    i = 0
    low = 0
    high = len(input_list) - 1

    while high >= i:
        if input_list[i] == 0:
            input_list[low], input_list[i] = input_list[i], input_list[low]
            low += 1
            i += 1
        elif input_list[i] == 1:
            i += 1
        else:
            input_list[i], input_list[high] = input_list[high], input_list[i]
            high -= 1

    print(input_list)


Input_list = [0, 1, 2, 0, 2, 2, 1, 0, 1, 0, 0]
print(f'Input: {Input_list}')

solution(Input_list)
