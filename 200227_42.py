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

    def _insert_value(self, node, data):
        if node is None:
            return Node(data)
        else:
            if node.data > data:
                node.left = self._insert_value(node.left, data)
            else:
                node.right = self._insert_value(node.right, data)

        return node

    def print(self):
        print_list = []
        self._print_tree(self.root, print_list)
        print(print_list)

    def _print_tree(self, node, print_list):
        if node is None:
            print("Node is None")
        else:
            if node.left is not None:
                self._print_tree(node.left, print_list)
            print_list.append(node.data)
            if node.right is not None:
                self._print_tree(node.right, print_list)


def get_leaf_node(node):
    if node is None:
        return 0
    if node.left is None and node.right is None:
        return 1
    else:
        return get_leaf_node(node.left) + get_leaf_node(node.right)


b_tree = BinarySearchTree()
b_tree.insert(17)
b_tree.insert(5)
b_tree.insert(4)
b_tree.insert(9)
b_tree.insert(20)

result = get_leaf_node(b_tree.root)
print(f'Count of Leaf node is {result}')
