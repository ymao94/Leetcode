# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        def explore(current_depth,node):
            if node:
                self.record.append(current_depth)
                explore(current_depth+1,node.left)
                explore(current_depth+1,node.right)
        self.record = []
        explore(1,root)
        if not self.record:
            return 0
        else:
            return max(self.record)

'''
record the depth of every node
'''
