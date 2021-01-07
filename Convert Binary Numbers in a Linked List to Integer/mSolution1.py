# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        if head:
            power = 0
            a = head
            while a.next:
                power += 1
                a = a.next
        value = 0
        a = head
        while power >= 0:
            value += a.val * (2 ** power)
            a = a.next
            power -=1
        return value
        
