class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class Binary_tree(object):
    def __init__(self):
        self.root = None

    def insert(self, data):
        self.root = self._insert_value(self.root, data)
        return self.root is not None

    def _insert_value(self,node, data):
        if node is None:
            node = Node(data)
        else:
            if data <= node.data:
                node.left = self._insert_value(node.left, data)
            else:
                node.right = self._insert_value(node.right, data)
        return node

    def print(self):
        print_list = []
        self._print_tree(self.root, print_list)
        print(print_list)

    def _print_tree(self, node, print_list):
        if node.left is not None:
            self._print_tree(node.left, print_list)
        print_list.append(node.data)
        if node.right is not None:
            self._print_tree(node.right, print_list)



def btr_reverse(node):
    if node is None:
        return None

    right = btr_reverse(node.right)
    left = btr_reverse(node.left)
    node.left = right
    node.right = left

    return node


Input_list = [21, 28, 14, 32, 25, 18, 11, 30, 19, 15]
Btr = Binary_tree()
for x in Input_list:
    Btr.insert(x)

Btr.print()

reverse_node = btr_reverse(Btr.root)
Btr.print()
