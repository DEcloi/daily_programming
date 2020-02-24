def solution(input_list, k):
    def reverse(start, end):
        while end > start:
            input_list[start], input_list[end] = input_list[end], input_list[start]
            start += 1
            end -= 1

    list_len = len(input_list)
    reverse(0, k-1)
    reverse(k, list_len-1)
    reverse(0, list_len-1)


Input_list = [1, 2, 3, 4, 5]
k = 2
print(f'Input: {Input_list}, k = {k}')

solution(Input_list, k)
print(f'Output: {Input_list}')
