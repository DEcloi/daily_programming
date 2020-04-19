def solution(input_list):
    start = 0
    end = len(input_list) - 1
    while end >= start:
        mid = (start + end) // 2
        if input_list[mid] == mid:
            return mid
        elif input_list[mid] > mid:
            end = mid - 1
        elif mid > input_list[mid]:
            start = mid + 1

    return "Not Found"


Input_list = [-30, 0, 1, 4, 60, 80]
print(f'Input: {Input_list}')

result = solution(Input_list)
print(f'Output: {result}')
