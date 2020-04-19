def swap(input_list, a, b):
    if a == b:
        return False
    temp = input_list[a]
    input_list[a] = input_list[b]
    input_list[b] = temp


def moving_zero(input_list):
    zero_index = 0
    for cur_index, value in enumerate(input_list):
        if value != 0:
            swap(input_list, cur_index, zero_index)
            zero_index += 1

    return input_list


Input_list1 = [0, 5, 0, 3, -1]
Input_list2 = [3, 0, 3]
print("Input:", Input_list1)

result = moving_zero(Input_list1)
print("Output:", result)
