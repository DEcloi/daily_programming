def reverse(Input_string):
    split_string = Input_string.split()

    # use reversed function
    reverse_string = ""
    for word in split_string:
        reverse_string += "".join(reversed(word)) + " "

    # Python style
    # for word in split_string:
    #     reverse_string += word[::-1] + " "

    return reverse_string


Input_string = "abc 123 apple"

result = reverse(Input_string)
print("Input:", Input_string)
print("Output:", result)
