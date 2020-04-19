N = 35

fibo_1 = 0
fibo_2 = 1

result = 0
while fibo_2 < N:
    if fibo_2 % 2 == 0:
        result += fibo_2

    temp = fibo_1 + fibo_2
    fibo_1 = fibo_2
    fibo_2 = temp
    # print(temp)

print(result)
