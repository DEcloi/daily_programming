import heapq

class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinarySearchTree(object):
    def __init__(self):
        self.root = None

    def insert(self, data):
        self.root = self._insert_value(self.root, data)
        return self.root is not None

    def _insert_value(self, node, data):
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


def solution(root):
    forward = [root]
    backward = []

    while backward or forward:
        while forward:
            tmp = forward.pop()
            print(tmp.data)

            if tmp.left:
                backward.append(tmp.left)
            if tmp.right:
                backward.append(tmp.right)

        while backward:
            tmp = backward.pop()
            print(tmp.data)

            if tmp.right:
                forward.append(tmp.right)
            if tmp.left:
                forward.append(tmp.left)



b_tree = BinarySearchTree()
b_tree.insert(21)
b_tree.insert(28)
b_tree.insert(14)
b_tree.insert(32)
b_tree.insert(25)
b_tree.insert(18)
b_tree.insert(11)
b_tree.print()

solution(b_tree.root)
