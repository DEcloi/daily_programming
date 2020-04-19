import copy

def solution(input_string):
    def print_string(out, str_list):
        if len(str_list) == 0:
            print(out)
            return

        temp_list = copy.deepcopy(str_list)
        for i in range(len(str_list)):
            del temp_list[i]
            print_string(out + str_list[i], temp_list)
            temp_list = copy.deepcopy(str_list)

    str_list = list(input_string)
    print_string('', str_list)


Input_string = 'ABC'
print(f'Input: {Input_string}')

solution(Input_string)
