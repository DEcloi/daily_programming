def solution(input_list):
    n = len(input_list) + 1
    x = int(n * (n + 1) / 2)
    y = sum(input_list)
    return x - y


Input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 15, 16, 17, 18, 19, 20]
N = 20
result = solution(Input_list)
print(f"{result} is missing")
