"""Given a binary tree, determine if it is height-balanced.
Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: true
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
result = True


def postOrder(root):
    left = 0
    right = 0
    if root == None:
        return 0
    left = postOrder(root.left)
    if left == -1:
        return -1
    right = postOrder(root.right)
    if right == -1:
        return -1

    if abs(left - right) > 1:
        return -1

    return 1 + max(left, right)


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        n = 0
        # m = 0
        if root == None:
            return True
        # n = postOrder(root)

        return postOrder(root) != -1