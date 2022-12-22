"""Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path
such that adding up all the values along the path equals targetSum.
A leaf is a node with no children.
Example 1:
Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
Output: true
Explanation: The root-to-leaf path with the target sum is shown.
"""

# Solution 1
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def checkSum(root, target):
    if root == None and target != 0:
        return False
    if root == None and target == 0:
        return False
    if root.left == None and root.right == None and target - root.val == 0:
        return True
    if root.left == None and root.right == None and target - root.val != 0:
        return False
    return checkSum(root.left, target - root.val) or checkSum(root.right, target - root.val)

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        return checkSum(root,targetSum)