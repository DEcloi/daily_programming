class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList(object):
    def __init__(self):
        self.head = None

    def insert(self, data):
        self._insert_value(self.head, data)

    def _insert_value(self, node, data):
        if node is None:
            self.head = Node(data)
        else:
            current = node
            while current.next is not None:
                current = current.next
            current.next = Node(data)

    def print(self):
        self._print_list(self.head)

    def _print_list(self, node):
        if node is None:
            print('LinkedList is None')
        else:
            current = node
            print_list = ''
            print_list += f'{current.data}'
            while current.next is not None:
                current = current.next
                print_list += f' > {current.data}'

            print(print_list)


def solution(node):
    pointer1 = pointer2 = node
    while pointer1:
        pointer2 = pointer1
        total = 0
        skip = False
        while pointer2:
            total += pointer2.data
            if total == 0:
                pointer1 = pointer2
                skip = True
                break
            pointer2 = pointer2.next

        if skip is False:
            print(pointer1.data)

        pointer1 = pointer1.next


l_list = LinkedList()
l_list.insert(1)
l_list.insert(2)
l_list.insert(3)
l_list.insert(4)
l_list.insert(-4)
l_list.insert(5)
l_list.insert(-5)
l_list.print()

solution(l_list.head)
