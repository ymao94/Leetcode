# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        def sums(root):
            if root:
                if low <= root.val <= high:
                    self.summe += root.val
                if low < root.val:
                    sums(root.left)
                if root.val < high:
                    sums(root.right)
        self.summe = 0
        sums(root)
        return self.summe

'''
recursive
dfs
self....here is important
'''
