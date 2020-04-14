# 11/06/2019


def solution(input_list, cost):
    def countPath(m, n, cost):
        if cost < 0:
            return 0

        if m == 0 and n == 0:
            if input_list[0][0] - cost == 0:
                return 1
            else:
                return 0

        key = f'{m} | {n} | {cost}'

        if key not in result_key:
            if m == 0:
                result_key[key] = countPath(0, n - 1, cost - input_list[m][n])
            elif n == 0:
                result_key[key] = countPath(m - 1, 0, cost - input_list[m][n])
            else:
                result_key[key] = countPath(m - 1, n, cost - input_list[m][n]) + \
                                  countPath(m, n - 1, cost - input_list[m][n])

        return result_key[key]

    result_key = dict()
    m = len(input_list) - 1
    n = len(input_list[0]) - 1

    return countPath(m, n, cost)


Input_list = [[4, 7, 1, 6],
              [5, 7, 3, 9],
              [3, 2, 1, 2],
              [7, 1, 6, 3]]
Cost = 25
print(f'Input: mat = {Input_list[0]}')
for i in Input_list[1:]:
    print(f'\t\t\t {i}')
print(f'\t   cost = {Cost}')

result = solution(Input_list, Cost)
print(f'Output: {result}')
