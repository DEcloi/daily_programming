# 10/13/2019
import random


def solution(input_list):
    random.shuffle(input_list)


def shuffle(input_list):
    for index in range(len(input_list)):
        rand_index = random.randrange(index, len(input_list))
        input_list[index], input_list[rand_index] = input_list[rand_index], input_list[index]


Input_list = [1, 2, 3, 4, 5, 6]
print(f'Input: {Input_list}')

# solution(Input_list)
# print(f'Output: {Input_list}')

shuffle(Input_list)
print(f'Output: {Input_list}')
