# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head   # goes to the end of the list
        p = self.reverseList(head.next) # don't forget the self. term!
        head.next.next = head    # reverse the order
        head.next = None  # remove the original link
        return p

'''
nice recursive algorithm
it first goes to the end of the linked list
then changes the order
'''
