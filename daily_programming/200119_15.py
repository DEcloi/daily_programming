class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.current = None

        self.num_of_node = 0

    def append(self, node):
        if self.head is None:
            self.head = node
            self.current = self.head
            self.before = self.head
        else:
            self.current.next = node
            self.current = self.current.next

        self.num_of_node += 1

    def print(self):
        if self.head is None:
            return "null"

        current = self.head
        print_str = f"{current.data}"

        while current.next is not None:
            current = current.next
            print_str += f" > {current.data}"

        return print_str


def solution(head, n):
    head1 = head
    head2 = head

    for i in range(n):
        head1 = head1.next

    while head1.next is not None:
        head1 = head1.next
        head2 = head2.next

    head2.next = head2.next.next


l_list = LinkedList()
l_list.append(Node(1))
l_list.append(Node(2))
l_list.append(Node(3))
l_list.append(Node(4))
l_list.append(Node(5))

N = 2
print(f"Input: {l_list.print()}, N={N}")

solution(l_list.head, N)
print(f"Output: {l_list.print()}")
