class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def RemoveNthnodefromend(head:None,n):
    slow = fast = head
    for _ in range(n):
        if not fast:
            raise ValueError("N is larger than Linked List")
        fast = fast.next
    if fast is None:
        return head.next
    while fast.next:
        slow = slow.next
        fast = fast.next
    slow.next = slow.next.next
    return head

