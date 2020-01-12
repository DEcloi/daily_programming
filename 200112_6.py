def interval(Input_list):
    Input_list = sorted(Input_list)

    index = 0
    result = [Input_list[0]]
    for cur_list in Input_list[1:]:
        if result[index][1] >= cur_list[0]:
            if result[index][1] < cur_list[1]:
                result[index][1] = cur_list[1]
        else:
            result.append(cur_list)
            index += 1

    return result


Input_list = [[2, 4], [1, 5], [7, 9]]
Input_list2 = [[3, 6], [1, 3], [2, 4]]

print(interval(Input_list2))
