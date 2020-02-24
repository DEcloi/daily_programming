def solution(input_list):
    def sort(start, end):
        if end <= start:
            return

        mid = partition(start, end)
        sort(start, mid - 1)
        sort(mid, end)

    def partition(start, end):
        pivot = input_list[(start + end) // 2]
        while start <= end:
            while input_list[start] < pivot:
                start += 1
            while input_list[end] > pivot:
                end -= 1
            if start <= end:
                input_list[start], input_list[end] = input_list[end], input_list[start]
                start, end = start + 1, end - 1

        return start

    return sort(0, len(input_list) - 1)


Input_list = [3, 2, 5, 1, 4]
print(f'Input: {Input_list}')

solution(Input_list)
print(f'Output: {Input_list}')
