# 11/13/2019


def solution(input_list, s):
    for index in range(len(input_list)):
        if input_list[index] > s:
            return False
        s -= input_list[index]
        if s == 0:
            return True
        else:
            return solution(input_list[index:], s)



def memoization(input_list, s):
    def dp(n, s):
        if s == 0:
            return True

        if n < 0 or s < 0:
            return False

        key = f'{n} | {s}'
        if key not in dp_dict:
            include = dp(n - 1, s - input_list[n])
            exclude = dp(n - 1, s)
            dp_dict[key] = (include or exclude)

        return dp_dict[key]

    dp_dict = dict()
    return dp(len(input_list) - 1, s)


Input_list = [7, 3, 2, 5, 8]
S = 14
print(f'Input: A = {Input_list}, s = {S}')

result = memoization(Input_list, S)
if result:
    print(f'Output: Yes')
else:
    print(f'Output: No')
