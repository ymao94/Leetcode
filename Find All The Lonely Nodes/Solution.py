# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getLonelyNodes(self, root: TreeNode) -> List[int]:
        self.list = []

        def mProgram(root):
            if not root.left and root.right:
                self.list.append(root.right.val)
            
            elif not root.right and root.left:
                self.list.append(root.left.val)
            
            
            if root.left:
                mProgram(root.left)
            if root.right:
                mProgram(root.right)
            
                
        mProgram(root)
        return self.list
