# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        slow = fast = revs = head
        while fast and fast.next:
            fast = fast.next.next
            temp = revs
            tems = slow.next
            revs = slow
            revs.next = temp
            slow = tems
            # or revs, revs.next, slow = slow, revs, slow.next
        if fast:
            slow = slow.next
#        while revs and revs.val == slow.val:
#            slow = slow.next
#            revs = revs.next
#        return not revs
        while slow:
            if slow.val != revs.val:
                return False
                break
            else:
                slow = slow.next
                revs = revs.next
        return True    

'''
what I have learnt from solving this problem:
1. Be careful to use recursion when you need to return a value in the function:
the returned value could be fixed during the first run!
2. Be careful to play with the linked list nodes. A former assignment could ruin
the rest of the code.
'''
