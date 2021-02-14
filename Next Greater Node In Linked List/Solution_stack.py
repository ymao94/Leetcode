# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        res = []
        stack = []
        i = 0
        val = []
        while head:
            res.append(0)
            val.append(head.val)
            while stack and val[stack[-1]] < head.val:
                res[stack.pop()] = head.val
            stack.append(i)
            i += 1
            head = head.next
        return res
           

'''
here I use the solution of normal Next Greater Value problem
The values are stored in a list
''' 
