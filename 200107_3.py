def a_func(x, y, string):
    if x == 0 and y == 0:
        print(string)
        return
    elif x == y:
        a_func(x-1, y, string + "(")
    elif x == 0:
        a_func(x, y-1, string + ")")
    else:
        a_func(x-1, y, string + "(")
        a_func(x, y-1, string + ")")

N = 3
open = N - 1
close = N

start_string = "("

a_func(open, close, start_string)
