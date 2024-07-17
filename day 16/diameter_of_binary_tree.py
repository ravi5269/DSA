# Diameter of Binary Tree
# Easy
# Given the root of a binary tree, return the length of the diameter of the tree.
# The diameter of a binary tree is the length of the longest path between
# any two nodes in a tree. This path may or may not pass through the root

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def diameter_Of_binarytree(root: TreeNode) -> int:
    def dfs(node: TreeNode) -> int:
        nonlocal diameter
        if not node:
            return 0
        
        left_depth = dfs(node.left)
        right_depth = dfs(node.right)
        
        # Update the diameter with the maximum path length found
        diameter = max(diameter, left_depth + right_depth)
        
        # Return the height of the current node
        return max(left_depth, right_depth) + 1
    
    diameter = 0
    dfs(root)
    return diameter

# Example usage:
# Constructing the binary tree:
#        1
#       / \
#      2   3
#     / \
#    4   5
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

# Calling the function
print(diameter_Of_binarytree(root))  # Output: 3
