""""Given a binary tree, find its minimum depth.The minimum depth is the number of nodes along the shortest
path from the root node down to the nearest leaf node.
Note:A leaf is a node with no children.
Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: 2"""

# Solution 1
def minDepth(root):
    if root == None:
        return 0

    left = minDepth(root.left)
    right = minDepth(root.right)

    if left == 0 and right == 0:
        return 1
    elif left == 0:
        return 1 + right
    elif right == 0:
        return 1 + left

    return 1 + min(left, right)


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        return minDepth(root)

# Solution 2
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def minidepth(root):
    if root == None:
        return 0
    if root.left == None and root.right == None:
        return 1
    if root.left == None:
        return minidepth(root.right) + 1
    if root.right == None:
        return minidepth(root.left) + 1
    else:
        return min(minidepth(root.left) , minidepth(root.right)) + 1

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        return minidepth(root)