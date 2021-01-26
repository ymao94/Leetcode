# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        pointer = list1
        for i in range(a-1):
            pointer = pointer.next
        cute = pointer.next
        pointer.next = list2
        while pointer.next:
            pointer = pointer.next
        for i in range(a,b):
            cute = cute.next
        pointer.next = cute.next
        return list1
       

# straightforward solution, run the nodes of the new linked list sequentially 
