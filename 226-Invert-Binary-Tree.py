"""226. Invert Binary Tree
Given the root of a binary tree, invert the tree, and return its root.
Example 1:
Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#

# Solution 1
def swapTree(root):
    if root == None:
        return
    root.left, root.right = swapTree(root.right), swapTree(root.left)
    return root
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        return swapTree(root)

#Solution 2
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                node.left, node.right = node.right, node.left
                stack += node.left, node.right
        return root