class ListNode:
    def __inti__(self,val=0,next=None):
        self.val=val
        self.next = next

def detectCycle(head: ListNode)-> ListNode:
    slow = head 
    fast = head 
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast :
            return findCycleStart(head,slow)
    return None

def findCycleStart(head:ListNode , meeting_node: ListNode) -> ListNode:
    pointer1 = head
    pointer2 = meeting_node
    while pointer1!= pointer2:
        pointer1 = pointer1.next
        pointer2 = pointer2.next
    return pointer1

