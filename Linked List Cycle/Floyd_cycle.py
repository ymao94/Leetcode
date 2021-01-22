# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        fast = slow = head
        while slow is not None:
            if fast is None or fast.next is None:
                return False
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        return False
