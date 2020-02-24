def solution(input_str):
    stack = []
    input_str = input_str.split("/")

    for i in input_str:
        if i == ".":
            continue
        elif i == "..":
            if len(stack) > 1:
                stack.pop()
        else:
            stack.append(i)

    return "/".join(stack)


Input_str = "/usr/./bin/./test/../"
print(f'Input: {Input_str}')

result = solution(Input_str)
print(f'Output: {result}')
