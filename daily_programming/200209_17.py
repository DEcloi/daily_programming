from collections import deque

def find_road(input_list, start, finish):
    recall = start
    current = start
    print(start)
    print(finish)
    
    if start[0] != finish[0] and start[1] != finish[1]:


    return False



Input_list = [[1, 0, 0, 1, 1, 0],
              [1, 0, 0, 1, 0, 0],
              [1, 1, 1, 1, 0, 0],
              [1, 0, 0, 0, 0, 1],
              [1, 1, 1, 1, 1, 1]]
Start = (0, 0)
Finish = (0, 4)

result = find_road(Input_list, Start, Finish)
print(f"Input: {Input_list}")
print(f"Start: {Start}")
print(f"Finish: {Finish}")
print(f"Output: {result}")
