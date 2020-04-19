def get_GCD(input_list):
    def gcd(a, b):
        if a == 0:
            return b

        return gcd(b % a, a)

    result = input_list[0]
    for i in range(1, len(input_list)):
        result = gcd(input_list[i], result)

    return result


Input_list = [10, 5]
print(f'Input: {Input_list}')

result = get_GCD(Input_list)
print(f'Output: {result}')
