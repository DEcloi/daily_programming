class Node(object):
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LinkedList(object):
    def __init__(self):
        self.head = None

    def insert(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = Node(data)

    def print(self):
        if self.head is None:
            print('Linked List is None')
            return
        else:
            current = self.head
            print_str = f'{current.data}'
            while current.next is not None:
                current = current.next
                print_str += f' > {current.data}'

            print(f'{print_str}')


def solution(node):
    if node is None:
        return

    temp_data = [node.data]
    current = node
    while current.next is not None:
        current = current.next
        temp_data.append(current.data)

    start = 0
    end = len(temp_data) - 1
    l_list = LinkedList()
    for i in range(len(temp_data)):
        if end >= start:
            if i % 2 == 0:
                l_list.insert(temp_data[start])
                start += 1
            else:
                l_list.insert(temp_data[end])
                end -= 1

    l_list.print()
    return


l_list = LinkedList()
l_list.insert(1)
l_list.insert(2)
l_list.insert(3)
l_list.insert(4)
l_list.insert(5)
l_list.insert(6)
l_list.insert(7)
l_list.insert(8)
l_list.insert(9)
l_list.print()

solution(l_list.head)
