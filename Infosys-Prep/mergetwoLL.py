class Node:
    def __inti__(self,data):
        self.data = data
        self.next = None
def mergeListNode(l1:Node,l2:Node):
    dummy = Node
    tail = dummy
    while l1 and l2:
        if l1.data>= l2.data:
            tail.next = l2
            l1 = l1.next
        else:
            tail.next = l1
            l2 = l2.next
        tail = tail.next
    tail.next = l1 if l1 else l2
    return dummy.next