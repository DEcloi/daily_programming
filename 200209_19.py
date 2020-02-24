def hurricane_print(input_list):
    list_rows = len(input_list)
    list_cols = len(input_list[0])
    list_size = list_rows * list_rows
    rows = 0
    cols = 0
    rows_arrow = 1
    cols_arrow = 1
    default_rows = 0
    default_cols = 0
    for x in range(list_size):
        s = rows_arrow + cols_arrow
        print(input_list[rows][cols])
        if s > 0:
            cols += cols_arrow
            if cols == list_cols - 1:
                cols_arrow = -1
        elif s < 0:
            cols += cols_arrow
            if cols == default_cols:
                cols_arrow = 1
                cols += 1
                default_cols += 1
        elif s == 0 and cols_arrow == -1:
            rows += rows_arrow
            if rows == list_rows - 1:
                rows_arrow = -1
        elif s == 0 and rows_arrow == -1:
            rows += rows_arrow
            if rows == default_rows:
                rows_arrow = 1
                rows += 1
                default_rows += 1

Input_list = [[1, 2, 3, 4], [12, 13, 14, 5], [11, 16, 15, 6], [10, 9, 8, 7]]
print(f'Input: {Input_list}')
hurricane_print(Input_list)
