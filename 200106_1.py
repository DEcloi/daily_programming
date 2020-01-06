a = [-1, 3, -1, 5]
b = [-5, -3, -1]
c = [2, 4, -2, -3, 8]
d = [-1, 4, -2, -3, 8]

cur_list = d

sum_value = cur_list[0]
max_value = cur_list[0]
for i in range(1, len(cur_list)):
    # print(cur_list[i], sum_value + cur_list[i])
    sum_value = max(cur_list[i], sum_value + cur_list[i])
    # print(sum_value, max_value)
    max_value = max(sum_value, max_value)

print("max value is", max_value)
