# 11/20/2019


def solution(input_list, target):
    pre_index = -1
    end_index = -1

    left = 0
    right = len(input_list) - 1
    while left <= right:
        mid = (left + right) // 2
        if input_list[mid] == target:
            pre_index = mid
            right = mid - 1
        elif input_list[mid] > target:
            right = mid - 1
        else:
            left = mid + 1

    left = 0
    right = len(input_list) - 1
    while left <= right:
        mid = (left + right) // 2
        if input_list[mid] == target:
            end_index = mid
            left = mid + 1
        elif input_list[mid] > target:
            right = mid - 1
        else:
            left = mid + 1

    return [pre_index, end_index]


Input_list = [2, 5, 5, 5, 6, 6, 8, 9, 9, 9]
Target = 2
print(f'Input:')
print(f'A = {Input_list}')
print(f'target = {Target}')

index = solution(Input_list, Target)
print(f'Output:')
if index[0] == -1 and index[1] == -1:
    print(f'찾는 값 없음')
else:
    print(f'첫 번째 위치는 인덱스 {index[0]}')
    print(f'마지막 위치는 인덱스 {index[1]}')
