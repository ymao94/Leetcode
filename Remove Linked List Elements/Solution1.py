# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if not head:  # Corner case: when the linked list is empty
            return None
        while head.val == val: # make sure the first element does not have val
                               # as value
            if head.next:      # delete the node
                head.val = head.next.val
                head.next = head.next.next
            else:
                return None    # if all the elements have val as value, then
                               # return an empty LL
        p = head #ignore the first element
        while p.next:
            if p.next.val == val:
                p.next = p.next.next
            else:
                p = p.next
        return head
       

'''
The task is not head, but one must be very careful with corner cases.
''' 
