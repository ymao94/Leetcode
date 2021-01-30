# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        vallist = []
        pointer = head
        while pointer:
            vallist.append(pointer.val)
            pointer = pointer.next
        vallist.sort()
        pointer = head
        for i in range(len(vallist)):
            pointer.val = vallist[i]
            pointer = pointer.next
        return head

'''
easy solution, quite quick.
But the memory needed is not constant.
'''
