def solution(input_list):

    index = 0
    for loop in range(len(input_list)):
        index = input_list[index]
        print(index, loop)
        if index == 0 and loop == (len(input_list)-1):
            return True

    return False


Input_list1 = [1, 2, 4, 0, 3]
Input_list2 = [1, 4, 5, 0, 3, 2]
print(f'Input: {Input_list2}')

result = solution(Input_list2)
print(f'Output: {result}')
