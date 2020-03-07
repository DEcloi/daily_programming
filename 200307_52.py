class Node(object):
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next


class DoublyLinkedList(object):
    def __init__(self):
        self.head = None

    def add(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            new_node.prev = current

    def search(self, value):
        if self.head is None:
            print(f'Linked List is None')
            return
        else:
            current = self.head
            if current.data == value:
                return current

            while current.next is not None:
                current = current.next
                if current.data == value:
                    return current

            if current.data == value:
                return current

    def remove(self, node):
        prev_node = node.prev
        prev_node.next = node.next
        del node

    def print(self):
        current = self.head
        print_str = f'{current.data}'
        while current.next is not None:
            current = current.next
            print_str += f' > {current.data}'

        print(print_str)


dl_list = DoublyLinkedList()
dl_list.add(1)
dl_list.add(2)
dl_list.add(3)
dl_list.add(4)
dl_list.add(5)
dl_list.print()

dl_list.remove(dl_list.search(4))
dl_list.print()
