# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        pointer = head
        been_here = []
        while pointer is not None:
            if pointer in been_here:
                return True
            else:
                been_here.append(pointer)
            pointer = pointer.next
        return False
