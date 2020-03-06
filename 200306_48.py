class Node(object):
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LinkedList(object):
    def __init__(self):
        self.head = None

    def input(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            current = self.head
            while current.next:
                current = current.next

            current.next = Node(data)

    def print(self):
        if self.head is None:
            print("Linked List is None")
            return
        else:
            current = self.head
            print_string = f'{current.data}'
            while current.next:
                current = current.next
                print_string += f' > {current.data}'

            print(print_string)


def solution(node):
    pointer1 = node
    pointer2 = node

    while pointer1.next is not None and pointer1.next.next is not None:
        pointer1 = pointer1.next.next
        pointer2 = pointer2.next

    print(pointer2.data)


l_list = LinkedList()
l_list.input(1)
l_list.input(2)
l_list.input(3)
l_list.input(4)
l_list.input(5)
l_list.input(6)
l_list.input(7)
l_list.input(8)
l_list.print()

solution(l_list.head)
