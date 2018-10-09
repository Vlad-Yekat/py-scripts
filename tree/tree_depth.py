class Node:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None


def min_depth(root):
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return 1
    if root.left is None:
        return min_depth(root.right)+1
    if root.right is None:
        return min_depth(root.left)+1

    return min(min_depth(root.left),min_depth(root.right))+1


root = Node(1)
root.left = Node(2)
root.left.left = Node(3)
print(min_depth(root))