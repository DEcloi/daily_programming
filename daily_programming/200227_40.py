def solution(num):
    print(num)
    str_num = str(num)
    current_num = str_num[0]
    count = 1
    result = ''
    for i in str_num[1:]:
        if i == current_num:
            count += 1
        else:
            result += f'{count}개의 {current_num}, '
            current_num = i
            count = 1

    result += f'{count}개의 {current_num}'

    return result


Input_num = 11231211
result = solution(Input_num)
print(f'{Input_num} - {result}')
