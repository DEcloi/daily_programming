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
            while current.next:
                current = current.next
            current.next = Node(data)

    def print(self):
        if self.head is None:
            print("Linked List is None")
            return
        else:
            current = self.head
            print_str = f'{current.data}'
            while current.next:
                current = current.next
                print_str += f' > {current.data}'

            return print_str


def solution(node1, node2):
    node1_num = 0
    digit = 1
    while node1:
        node1_num += node1.data * digit
        digit *= 10
        node1 = node1.next

    node2_num = 0
    digit = 1
    while node2:
        node2_num += node2.data * digit
        digit *= 10
        node2 = node2.next

    total = node1_num + node2_num

    l_list = LinkedList()
    while total:
        remainder = total % 10
        total = total // 10
        l_list.insert(remainder)

    return l_list.print()

l_list1 = LinkedList()
l_list1.insert(1)
l_list1.insert(5)
l_list1.insert(6)

l_list2 = LinkedList()
l_list2.insert(0)
l_list2.insert(0)
l_list2.insert(4)

print(f'Input: {l_list1.print()}, {l_list2.print()}')

result = solution(l_list1.head, l_list2.head)
print(f'Output: {result}')
