import heapq

from collections import defaultdict


def solution(input_str):
    str_dict = defaultdict(int)
    for char in input_str:
        str_dict[char] += 1

    heap = []
    for char, count in str_dict.items():
        heapq.heappush(heap, (-count, char))

    count, char = heapq.heappop(heap)
    result = [char]

    while heap:
        last = (count + 1, char)
        print(heap)
        count, char = heapq.heappop(heap)
        result.append(char)

        if last[0] < 0:
            heapq.heappush(heap, last)

    if len(result) == len(input_str):
        return "".join(result)
    else:
        return ""


Input_str = 'aaabbcc'
print(f'Input: {Input_str}')

result = solution(Input_str)
print(f'Output: {result}')
