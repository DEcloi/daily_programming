# 09/15/2019

def solution(x, y):
    x_index = 0
    while x_index != len(x):
        y_index = 0
        if x[x_index] > y[y_index]:
            x[x_index], y[y_index] = y[y_index], x[x_index]
            while y[y_index] > y[y_index + 1]:
                y[y_index], y[y_index + 1] = y[y_index + 1], y[y_index]
                y_index += 1
                if y_index == (len(y) - 1):
                    break

        x_index += 1


X = [4, 7, 8, 10, 12, 19]
Y = [2, 3, 6, 15, 17]

print(f'Input')
print(f'{X}')
print(f'{Y}')

solution(X, Y)
print(f'Output')
print(f'{X}')
print(f'{Y}')
