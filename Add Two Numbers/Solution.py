# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        dummy = ListNode(0)
        curr = dummy
        while l1 and l2:
            val = l1.val + l2.val + carry
            curr.next = ListNode(val % 10)
            carry = int(val/10)
            l1, l2, curr = l1.next, l2.next, curr.next
        while l1:
            val = l1.val + carry
            curr.next = ListNode(val % 10)
            carry = int(val/10)
            l1, curr = l1.next, curr.next
        while l2:
            val = l2.val + carry
            curr.next = ListNode(val % 10)
            carry = int(val/10)
            l2, curr = l2.next, curr.next
        if carry == 1:
            curr.next = ListNode(carry)
        return dummy.next

'''
space complexity: O(max(m,n))
time complexity: O(max(m,n))
'''
