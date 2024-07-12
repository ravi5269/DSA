"""Lowest Common Ancestor of a Binary
Search Tree
Easy
Given a binary search tree (BST), find the lowest common ancestor (LCA) 

node of two given nodes in the BST.
According to the definition of LCA on Wikipedia: “The lowest common
ancestor is defined between two nodes
that has both p and q p and q
as the lowest node in
as descendants (where we allow a node to ).”
descendant of itself"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowest_common_ancestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        while root:
            # If both p and q are greater than root, then LCA lies in the right subtree
            if p.val > root.val and q.val > root.val:
                root = root.right
            # If both p and q are less than root, then LCA lies in the left subtree
            elif p.val < root.val and q.val < root.val:
                root = root.left
            else:
                # If we find a split point, i.e., root is the LCA
                return root

# Example 
if __name__ == "__main__":
    # Constructing a small BST
    #       3
    #      / \
    #     1   4
    #      \
    #       2

    root = TreeNode(3)
    root.left = TreeNode(1)
    root.right = TreeNode(4)
    root.left.right = TreeNode(2)

    p = root.left  # Node with value 1
    q = root.left.right  # Node with value 2

    solution = Solution()
    lca = solution.lowest_common_ancestor(root, p, q)
    print(f"The LCA of node {p.val} and node {q.val} is node {lca.val}.")
