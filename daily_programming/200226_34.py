def Quick_sort(input_list):
    def sort(start, end):
        if start >= end:
            return

        mid = partition(start, end)
        sort(start, mid - 1)
        sort(mid, end)

    def partition(start, end):
        pivot = input_list[(start + end) // 2]
        while start <= end:
            while pivot > input_list[start]:
                start += 1
            while input_list[end] > pivot:
                end -= 1
            if start <= end:
                input_list[start], input_list[end] = input_list[end], input_list[start]
                start += 1
                end -= 1

        return start

    sort(0, len(input_list) - 1)

def Merge_sort(input_list):
    def sort(list):
        if len(list) > 1:
            mid = len(list) // 2
            left = list[:mid]
            right = list[mid:]

            sort(left)
            sort(right)

            i=0
            j=0
            k=0
            while len(left) > i and len(right) > j:
                if right[j] > left[i]:
                    list[k] = left[i]
                    i += 1
                else:
                    list[k] = right[j]
                    j += 1
                k += 1

            while len(left) > i:
                list[k] = left[i]
                i += 1
                k += 1

            while len(right) > j:
                list[k] = right[j]
                j += 1
                k += 1

    sort(input_list)


Input_list = [7, 5, 3, 2, 6, 1, 9, 4, 8]
print(f'Input: {Input_list}')

# Quick_sort(Input_list)
Merge_sort(Input_list)
print(f'Output: {Input_list}')
