# 11/17/2019


def solution(input_string):
    temp_string = input_string
    best_string = input_string
    for i in range(len(input_string)):
        temp_string = temp_string[1:] + temp_string[0]
        for j in range(len(temp_string)):
            if ord(best_string[j]) > ord(temp_string[j]):
                best_string = temp_string
                break
            else:
                break

    return best_string


Input_string = 'bbaaccaadd'
print(f'Input: {Input_string}')

result = solution(Input_string)
print(f'Output: {result}')
