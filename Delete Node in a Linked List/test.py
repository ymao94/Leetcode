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


my_list = My_List(ListNode('start'))
dd = {} # use this dict to keep reference to each element
for i in range(5):
    dd[i] = ListNode('item-%s' %i)
    my_list.add(dd[i])
my_list.print()

print('sdfkaskfskfdsjfkdsjfkds')

nond = dd[2]
#nond.val = 3
nond.next = nond.next.next

my_list.print()

