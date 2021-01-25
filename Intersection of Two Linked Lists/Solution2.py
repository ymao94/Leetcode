# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        pA = headA
        pB = headB
        counter = 0 # when there is no intersection
        if pA is None or pB is None:
            return None
        while pA != pB and counter <2:
            if pA.next is None:
                pA = headB
                counter += 1
            else:
                pA = pA.next
            if pB.next is None:
                pB = headA
            else:
                pB = pB.next
        if counter <2:
            return pA
        else:
            return None

'''
used a trick:
start from both heads, when one list is traversed to the end, then the pointer
starts from the head of the other list.
Attention! Two corner cases: when one of the lists is empty or there is no
intersection.
'''
