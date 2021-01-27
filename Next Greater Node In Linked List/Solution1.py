# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        pointer = head
        list1 = []
        while pointer:
            list1.append(pointer.val)
            pointer = pointer.next
        for i in range(len(list1)-1):
            for j in range(i+1,len(list1)):
                if list1[i] < list1[j]:
                    list1[i] = list1[j]
                    break
                elif list1[i] >= list1[j] and j < len(list1)-1:
                    pass
                else:
                    list1[i] = 0
        list1[-1] = 0
       # pointer = head
       # for i in range(len(list1)):
       #     pointer.val = list1[i]
       #     pointer = pointer.next
       # return head
        return list1


'''
Remark:
actually this code failed to pass the test.
But I believe this code is valid, just not efficient enough.
'''
