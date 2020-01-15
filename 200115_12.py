def mul(input_list):
    cur = 1
    a_list = [cur]
    for i in range(len(input_list)-1):
        cur *= input_list[i]
        a_list.append(cur)

    cur = 1
    b_list = [cur]
    for i in range(len(input_list)-1, 0, -1):
        cur *= input_list[i]
        b_list.insert(0, cur)

    result = []
    for i in range(len(a_list)):
        result.append(a_list[i] * b_list[i])

    return result


Input_list = [1, 2, 3, 4, 5]

result = mul(Input_list)
print(f"Input: {Input_list}")
print(f"Output: {result}")
