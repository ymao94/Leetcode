# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        cute = head # keep track of the first node
        while head and head.next:
            if head.val == head.next.val: # detect the same value
                head.next = head.next.next # skip the next node, then the loop
                                           # would run again and move the the
                                           # 'else' option
            else:
                head = head.next  # move to the next step
        return cute
