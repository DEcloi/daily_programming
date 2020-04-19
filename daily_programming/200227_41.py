class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinarySearchTree(object):
    def __init__(self):
        self.root = None

    def insert(self, input_list):
        self.root = self._insert_value(input_list)

    def _insert_value(self, input_list):
        if not input_list:
            return None

        mid = (len(input_list)) // 2

        root = Node(input_list[mid])
        root.left = self._insert_value(input_list[:mid])
        root.right = self._insert_value(input_list[mid + 1:])

        return root

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


Input_list = [3, 5, 10, 15, 16, 19, 21, 33, 41, 50, 57, 72, 100, 111, 191]
print(f'Input: {Input_list}')

b_tree = BinarySearchTree()
b_tree.insert(Input_list)
b_tree.print()
