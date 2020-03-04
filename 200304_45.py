def solution(k):
    def print_string(k, out, last_digit):
        if k == 0:
            print(out)
            return

        print_string(k - 1, out + "0", 0)

        if last_digit == 0:
            print_string(k - 1, out + "1", 1)

    print_string(k, "", 0)


K = 5
print(f'Input: {K}')

solution(K)
