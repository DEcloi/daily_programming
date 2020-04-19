def solution(input_list, k):
    def pair_sums_to_k(input_list, k, start):
        lo = start
        hi = len(input_list) - 1
        while lo < hi:
            if input_list[lo] + input_list[hi] == k:
                return True
            elif input_list[lo] + input_list[hi] < k:
                lo += 1
            else:
                hi -= 1
        return False

    input_list.sort()
    for i in range(len(input_list) - 2):
        if pair_sums_to_k(input_list, k - input_list[i], i + 1):
            return True

    return False


Input_list = [3, 7, 10, 2, 5, 1]
K = 12

print(f'Input: {Input_list}, K: {K}')

result = solution(Input_list, K)
print(f'Output: {result}')
