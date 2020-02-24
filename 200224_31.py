import math
import heapq


def radixSort(input_list):
    def countingSort(exp1):
        n = len(input_list)
        output = [0] * (n)
        count = [0] * (10)

        for i in range(n):
            index = int((input_list[i] / exp1))
            count[(index) % 10] += 1

        for i in range(1, 10):
            count[i] += count[i - 1]
        print(count)

        i = n - 1
        while i >= 0:
            index = int((input_list[i] / exp1))
            output[count[(index) % 10] - 1] = input_list[i]
            count[(index) % 10] -= 1
            print(count)
            i -= 1

        i = 0
        for i in range(0, len(input_list)):
            input_list[i] = output[i]

    max1 = max(input_list)

    exp = 1
    while int(max1 / exp) > 0:
        countingSort(exp)
        exp *= 10



Input_list = [12, 13, 14]
print(f'Input: {Input_list}')

radixSort(Input_list)
print(f'Output: {Input_list}')
