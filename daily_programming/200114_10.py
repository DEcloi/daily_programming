def substring(str):
    str_list = []
    for char in str:
        if char not in str_list:
            str_list.append(char)

    return len(str_list), "".join(str_list)


Input_string = "aaabbbccceded"

len, result = substring(Input_string)
print(f"Input: {Input_string}")
print(f"Output: {len} // {result}")
