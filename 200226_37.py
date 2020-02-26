class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinarySearchTree(object):
    def __init__(self):
        self.root = None

    def insert(self, data):
        self.root = self._insert_data(self.root, data)

    def _insert_data(self, node, data):
        if node is None:
            return Node(data)
        else:
            if node.data >= data:
                node.left = self._insert_data(node.left, data)
            else:
                node.right = self._insert_data(node.right, data)

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


def solution(node, start, end):
    if node is None:
        return

    if node.data > start:
        solution(node.left, start, end)
    if start < node.data < end:
        print(node.data)
    if end > node.data:
        solution(node.right, start, end)


b_tree = BinarySearchTree()
b_tree.insert(17)
b_tree.insert(5)
b_tree.insert(9)
b_tree.insert(30)
b_tree.insert(1)
b_tree.print()

solution(b_tree.root, 1, 31)
