# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def merge(self, l1, l2):
        dummy = ListNode('start')
        curr = dummy
        while l1 and l2:
            if l1.val > l2.val:
                curr.next, l2 = l2, l2.next
            else:
                curr.next, l1 = l1, l1.next
            curr = curr.next
        if l1:
            curr.next = l1
        else:
            curr.next = l2
        return dummy.next
    
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        pointer = slow = fast = head
        while fast and fast.next:
            pointer, slow, fast = slow, slow.next, fast.next.next
        pointer.next = None
        
        return self.merge(self.sortList(head),self.sortList(slow)) # I still
#don't understand this so well.
                                                                    




# Merge Sort
