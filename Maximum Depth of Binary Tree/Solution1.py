# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        else:
            l = self.maxDepth(root.left) + 1
            r = self.maxDepth(root.right) + 1
            self.res = max(l,r)
        return self.res
