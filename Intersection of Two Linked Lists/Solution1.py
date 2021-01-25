# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        currA = headA
        currB = headB
        A = {} # I used a list, but is not efficient enough, I don't know why
        while currA is not None:
            A[currA] = currA # really useless information, don't know why it is
                             # more efficient than the List
            currA = currA.next
        while currB is not None:
            if currB in A:
                return currB    
            currB = currB.next
        return None

# First solution based on the first idea I got
# first traverse one LL, then compare the nodes in another LL one by one
