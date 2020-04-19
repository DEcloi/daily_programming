def search(Input_list, target):
    Input_dict = dict(zip(Input_list, range(len(Input_list))))

    # print(Input_dict)
    # for item in Input_dict.popitem():
    #     print(item)

    for value, index in Input_dict.items():
        set = target - value
        if set in Input_dict.keys():
            return [index, Input_dict[set]]

    return False


Input_list = [2, 5, 6, 1, 10]
target = 8

result = search(Input_list, target)
if result:
    print(result)
else:
    print("No solution")
