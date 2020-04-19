def big_number(input_list, target):
        sort_list = sorted(Input_list, reverse=True)

        return sort_list[target-1]


Input_list = [-1, 3, -1, 5, 4]
Target = 2

result = big_number(Input_list, Target)
print(f"Input: {Input_list}, {Target}")
print(f"Output: {result}")
