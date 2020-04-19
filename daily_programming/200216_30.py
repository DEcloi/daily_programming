def bit_counter(number):
    return bin(number)[2:].count('1')


Input_number = 6
print(f'Input: {Input_number}')

result = bit_counter(Input_number)
print(f'Output: {result}')
