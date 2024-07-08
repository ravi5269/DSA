
# Your implementation of the invertTree function in the Solution class is correct. 
# The function recursively inverts the binary tree by swapping the left and right children of each node.
#  Here's the code you provided,
#  with a slight correction to the Optional type hint from the typing module:


from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invert_tree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        if not root: return None

        self.invert_tree(root.left)
        self.invert_tree(root.right)
        temp = root.left
        root.left = root.right
        root.right = temp
        return root
    
def print_tree(root: TreeNode, depth=0):
    if root:
        print_tree(root.right, depth + 1)
        print(" " * 4 * depth + "->", root.val)
        print_tree(root.left, depth + 1)

root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(7)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right.left = TreeNode(6)
root.right.right = TreeNode(9)

print("Original tree:")
print_tree(root)
