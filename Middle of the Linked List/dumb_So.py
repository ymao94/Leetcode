# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        lens = 0
        pointer = head
        while pointer is not None:
            lens += 1
            pointer = pointer.next
        middle = int(lens/2) + 1
        while middle > 1:
            head = head.next
            middle -= 1
        while middle > 1:
            head = head.next
            middle -= 1
        return head
        
