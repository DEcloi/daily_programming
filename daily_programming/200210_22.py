def solution(input_list, target):
    start = 0
    end = len(input_list)

    while end >= start:
        pivot = (start + end) // 2
        if input_list[pivot] == target:
            return True
        elif input_list[pivot] < target:
            start = pivot + 1
        elif input_list[pivot] > target:
            end = pivot - 1

    return False


Input_list = [1, 2, 3, 7, 10]
target = 7
print(f'Input: {Input_list}')

result = solution(Input_list, target)
print(f'Output: {result}')
