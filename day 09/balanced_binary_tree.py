# Balanced Binary Tree
# Easy
# Given a binary tree, determine if it is height-balanced


# Checking if a binary tree is height balanced in Python


class Node:

    def __init__(self, data):
        self.data = data
        self.left = self.right = None


class Height:
    def __init__(self):
        self.height = 0


def balanced_binary(root, height):

    left_height = Height()
    right_height = Height()

    if root is None:
        return True

    l = balanced_binary(root.left, left_height)
    r = balanced_binary(root.right, right_height)

    height.height = max(left_height.height, right_height.height) + 1

    if abs(left_height.height - right_height.height) <= 1:
        return l and r

    return False


height = Height()

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

if balanced_binary(root, height):
    print('The tree is balanced')
else:
    print('The tree is not balanced')


# example
# Constructing a simple binary tree:
#       1
#      / \
#     2   3
#    / \
#   4   5