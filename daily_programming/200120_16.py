class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, node):
        if self.head is None:
            self.head = node
        else:
            current = self.head
            while current.next is not None:
                current = current.next

            current.next = node

    def print(self):
        if self.head is None:
            return "None"
        else:
            current = self.head
            print_str = f"{current.data}"
            while current.next is not None:
                current = current.next
                print_str += f" > {current.data}"

        return print_str


def linkedlist_sort(l_list1, l_list2):
    sort_list = LinkedList()
    l_list1_current = l_list1.head
    l_list2_current = l_list2.head

    while l_list1_current is not None and l_list2_current is not None:
        if l_list1_current.data > l_list2_current.data:
            sort_list.append(Node(l_list2_current.data))
            l_list2_current = l_list2_current.next
        else:
            sort_list.append(Node(l_list1_current.data))
            l_list1_current = l_list1_current.next

    if l_list1_current is None:
        while l_list2_current is not None:
            sort_list.append(Node(l_list2_current.data))
            l_list2_current = l_list2_current.next
    else:
        while l_list1_current is not None:
            sort_list.append(Node(l_list1_current.data))
            l_list1_current = l_list1_current.next

    return sort_list


l_list1 = LinkedList()
l_list1.append(Node(1))
l_list1.append(Node(3))
l_list1.append(Node(5))
l_list1.append(Node(6))

l_list2 = LinkedList()
l_list2.append(Node(2))
l_list2.append(Node(4))

print(f"Input: {l_list1.print()}, {l_list2.print()}")
result = linkedlist_sort(l_list1, l_list2)
print(f"Output: {result.print()}")
