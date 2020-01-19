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
        if self.num_of_node == 0:
            self.head = node
        else:
            current = self.head
            for _ in range(self.num_of_node - 1):
                current = current.next
            current.next = node

        self.num_of_node += 1

    def delete(self, node_num):
        before = self.head
        current = self.head
        for i in range(self.num_of_node - node_num):
            before = current
            current = current.next

        if current.next is None:
            before.next = None
            current = None
        else:
            before.next = current.next
            current = None

        self.num_of_node -= 1

    def print(self):
        if self.num_of_node == 0:
            return "null"

        current = self.head
        print_str = f"{current.data}"
        for _ in range(self.num_of_node - 1):
            current = current.next
            print_str += f" > {current.data}"

        return print_str


l_list = LinkedList()
l_list.append(Node(1))
l_list.append(Node(2))
l_list.append(Node(3))
l_list.append(Node(4))
l_list.append(Node(5))

N = 2
print(f"Input: {l_list.print()}, N={N}")

l_list.delete(N)
print(f"Output: {l_list.print()}")
