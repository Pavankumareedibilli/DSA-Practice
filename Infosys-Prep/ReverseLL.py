class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def reverse(head:Node):
    prev = None
    curr = head
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    return prev