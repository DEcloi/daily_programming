# 09/18/2019

def solution(x, y):
    empty_index = []
    x_index = 0
    y_index = 0
    while x_index != len(x):
        if x[x_index] == 0:
            empty_index.append(x_index)
            x_index += 1
        elif empty_index:
            if x[x_index] > y[y_index]:
                x[empty_index[0]] = y[y_index]
                empty_index.pop(0)
                y_index += 1
            else:
                x[empty_index[0]] = x[x_index]
                x[x_index] = 0
                empty_index.append(x_index)
                empty_index.pop(0)
                x_index += 1
        else:
            if x[x_index] > y[y_index]:
                x[x_index], y[y_index] = y[y_index], x[x_index]
                x_index += 1

    if empty_index:
        for i in empty_index:
            x[i] = y[y_index]
            y_index += 1


X = [0, 3, 0, 0, 0, 5, 6, 0, 0, 7, 13]
Y = [1, 2, 8, 9, 10, 15]

print('Input')
print(f'X = {X}')
print(f'Y = {Y}')

solution(X, Y)
print('Output')
print(f'X = {X}')
