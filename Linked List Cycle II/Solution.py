# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
#        if not head or not head.next:
#            return None
        fast = slow = head
        while slow:
            if not fast or not fast.next:
                return None
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                while slow != head:
                    slow, head = slow.next, head.next
                return head
        return None
            
        
