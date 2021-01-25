class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class My_List(object):

    def __init__(self, x):
        self.first_node = x
        self.last_node = x

    def add(self,x):
        self.last_node.next = x
        self.last_node = self.last_node.next

    def print(self):
        temp = self.first_node
        index = 1 
        while temp is not None:
            print('%s-%s' % (index, temp.val))
            temp = temp.next
            index +=1

class Solution:
    def deleteDuplicates(self, head):
        pointer = head
        if pointer is None:
            return pointer
        appeared = []
        while pointer is not None and pointer.next is not None:
#            if pointer.next is None:
#                print(pointer.val)
#                if pointer.val in appeared:
#                    pointer = pointer.next
#                else:
#                    print('aha`:')
#                    pointer = pointer.next
#            else:
             if pointer.val in appeared:
                 pointer.val = pointer.next.val
                 pointer.next = pointer.next.next
             else:
                 appeared.append(pointer.val)
                 pointer = pointer.next
                 print(appeared)
        return pointer


my_list = My_List(ListNode('start'))
dd = {} # use this dict to keep reference to each element
for i in range(5):
    dd[i] = ListNode('item-%s' %i)
    my_list.add(dd[i])


dd[0].val = 2
dd[1].val = 4
dd[3].next  = None
dd[2].val = 2
dd[3].val = 4
dd[4].val = 4
#nond.val = 3
#nond.next = nond.next.next
Solution().deleteDuplicates(dd[0])
my_list.print()

