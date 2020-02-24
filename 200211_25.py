def solution(input_list, k):
    def search(start, end):
        if start > end:
            return -1

        mid = (start + end) // 2
        if input_list[mid] == k:
            return mid

        if input_list[mid] >= input_list[start]:
            if k >= input_list[start] and input_list[mid] >= k:
                return search(start, mid-1)
            return search(mid+1, end)

        if k >= input_list[mid] and input_list[end] >= k:
            return search(mid+1, end)

        return search(start, mid-1)

    return search(0, len(input_list)-1)


Input_list1 = [3, 4, 5, 6, 7, 8, 9, 10, 11, 1, 2]
Input_list2 = [2, 4, 5, 1]
k = 3

print(f'Input: {Input_list2}')

result = solution(Input_list2, k)
print(f'Output: {result}')
