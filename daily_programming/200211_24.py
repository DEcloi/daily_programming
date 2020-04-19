class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList(object):
    def __init__(self):
        self.head = None

    def insert(self, data):
        if self.head is None:
            self.head = self._insert_Node(data)
        else:
            current = self.head
            while current.next is not None:
                current = current.next

            current.next = self._insert_Node(data)

    def _insert_Node(self, data):
        return Node(data)

    def print(self):
        print_str = ''
        if self.head is None:
            print("None")

        current = self.head
        while current.next is not None:
            current = self.head
            print_str = f'{current.data}'
            while current.next is not None:
                current = current.next
                print_str += f' > {current.data}'

        print(print_str)


def merge_sort(node):
    def sort(left, right):
        if left is None:
            return right
        if right is None:
            return left

        if left.data >= right.data:
            result = right
            result.next = sort(left, right.next)
        else:
            result = left
            result.next = sort(left.next, right)

        return result

    def get_Middle():
        if node is None:
            return node

        node1 = node.next
        node2 = node

        while node1 is not None:
            node1 = node1.next
            if node1 is not None:
                node2 = node2.next
                node1 = node1.next

        return node2

    if node is None or node.next is None:
        return node

    middle = get_Middle()
    middle_next = middle.next

    middle.next = None

    left = merge_sort(node)
    right = merge_sort(middle_next)

    head = sort(left, right)

    return head


L_list = LinkedList()
L_list.insert(7)
L_list.insert(3)
L_list.insert(1)
L_list.insert(5)
L_list.insert(6)
L_list.print()

L_list.head = merge_sort(L_list.head)
L_list.print()
