# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        ath = list1
        while a > 1:
            ath = ath.next
            a -= 1
        bth = list1.next
        while b>0:
            bth = bth.next
            b -= 1
        last = list2
        while last.next:
            last = last.next
        ath.next = list2
        last.next = bth
        return list1
       

# Most intuitive solution, succeeded at the first run 
