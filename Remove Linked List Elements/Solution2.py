# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if not head: # corner case: when the LL is empty
            return None
        else:
            if head.val == val: 
                head = self.removeElements(head.next,val)
                '''
                if the head is already val, then we ignore it
                if it is not, then we start from the next one
                '''
            else:
                head.next = self.removeElements(head.next,val)
        return head
       
'''
extremely cute recursion solution.
but expensive!
how high is the complexity?
O(n)
O(n)
'''

 
