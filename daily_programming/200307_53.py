def solution(input_list):
    def consecutive(i, j, max, min):
        if max - min != j - i:
            return False

        visited = input_list[i:j+1]
        print(i, j, visited)
        for k in range(i, j):
            if visited[input_list[k] - min]:
                return False

            visited[input_list[k] - min] = True

        return True

    list_len = 1
    start = 0
    end = 0
    for i in range(len(input_list)):
        max_num = input_list[i]
        min_num = input_list[i]
        for j in range(i+1, len(input_list)):
            max_num = max(input_list[j], max_num)
            min_num = min(input_list[j], min_num)

            if consecutive(i, j, max_num, min_num):
                if list_len < max_num - min_num + 1:
                    list_len = max_num - min_num + 1
                    start = i
                    end = j

    print(start, end)


Input_list = [2, 0, 2, 1, 4, 3, 1, 0]
print(f'Input: {Input_list}')

solution(Input_list)
