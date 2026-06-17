class ListNode:
    def __init__(self,val=0,next = None):
        self.val = val
        self.next = next
def cycleLength(head:ListNode) -> int:
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next

        if slow == fast :
            return cal_length(slow)    
    return 0

def cal_length(meeting_node : ListNode) -> bool:
    current_node = meeting_node
    length = 1

    while current_node.next != meeting_node:
        current_node=current_node.next
        length = length+1
    return length