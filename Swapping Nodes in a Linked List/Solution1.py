# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        pairA = pairB = head
        for i in range(k-1):
            pairB = pairB.next
        begin = pairB
        while pairB.next:
            pairA = pairA.next
            pairB = pairB.next
        begin.val, pairA.val = pairA.val, begin.val
        return head


# two pointers solution
