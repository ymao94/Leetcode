# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        list1 = []
        list2 = []
        while l1:
            list1.append(l1.val)
            l1 = l1.next
        while l2:
            list2.append(l2.val)
            l2 = l2.next
        v1 = v2 = 0
        for i in range(len(list1)):
            v1 += list1[i]* (10**i)
        for i in range(len(list2)):
            v2 += list2[i]* (10**i)
        v = v1 + v2
        v = [int(i) for i in str(v)]
        v.reverse()
        p = ListNode('s')
        vhead = p
        for i in range(len(v)):
            pi = ListNode('%s' %i)
            pi.val = v[i]
            p.next = pi
            p = p.next
        p.next = None
        return vhead.next

'''
ugly solution
poor performance
'''
