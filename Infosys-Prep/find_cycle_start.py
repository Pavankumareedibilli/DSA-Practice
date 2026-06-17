class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


def find_cycle_start(head:Node):
    slow = head
    fast = head
    #detect cycle

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            break
    else:
        return None
    
    #finding entry point
    slow = head

    while slow!=fast:
        slow = slow.next
        fast = fast.next
    return slow