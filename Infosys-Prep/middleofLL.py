class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def MiddleLL(Head:Node):
    slow = Head
    fast = Head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow
