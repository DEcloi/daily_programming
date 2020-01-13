def second_big_number(number_list):
    if number_list[0] > number_list[1]:
        first = number_list[0]
        second = number_list[1]
    else:
        first = number_list[0]
        second = number_list[1]

    for cur_num in number_list[1:]:
        if cur_num > second:
            if first > cur_num:
                second = cur_num
            else:
                second = first
                first = cur_num

    if first == second:
        return "Dose not exist."

    return second


number_list1 = [10, 5, 4, 3, -1]
number_list2 = [3, 3, 3]

result = second_big_number(number_list2)

print("Input:", number_list2)
print("Output:", result)
