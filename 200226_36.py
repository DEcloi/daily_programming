def solution(target):
    if 4 > target:
        return f'{target} is not a power of 4'
    elif target == 4:
        return f'{target} is a power of 4'

    quotient = target // 4
    remainder = target % 4
    while quotient > 4 and remainder == 0:
        quotient = quotient // 4
        remainder = target % 4

    if quotient == 4 and remainder == 0:
        return f'{target} is a power of 4'
    else:
        return f'{target} is not a power of 4'

target = 16
print(f'Input: {target}')

for i in range(0, 65):
    result = solution(i)
    print(f'Output: {result}')