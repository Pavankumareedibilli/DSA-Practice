class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def asCycle(head:Node):
    slow = head
    fast = head
    while fast and fast.next.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True
    return False