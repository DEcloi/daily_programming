def prefix(input_list):
    input_list.sort(key=len)
    for i in range(len(input_list[0])):
        for j in range(1, len(input_list)):
            if input_list[0][i] != input_list[j][i]:
                return i, input_list[0][:i]

    return i+1, input_list[0]


Input_list1 = ["apple", "apps", "ape"]
Input_list2 = ["hawaii", "happy"]
Input_list3 = ["dog", "doge", "dogs"]

print(f"Input: {Input_list3}")
prefix_len, prefix_word = prefix(Input_list3)
print(f"Output: {prefix_len} // {prefix_word}")
