# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None: # Corner case: when the LinkedList is empty
            return None
        new = head # the new reference
        old = head.next # the pointer that goes one step further
        new.next = None
        while old is not None:
            newt = new # temporal value to store the former reference
            new = old
            old = old.next  # the order is important, or
            new.next = newt # it would change the next reference of 'old'
            
        return new
       

'''
I felt like an absolute Genius!
figured it out without peeping into the solutions
''' 
