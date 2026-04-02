# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse second half
        nextNode = slow.next
        currNode = slow.next = None
        while nextNode:
            reserved = nextNode.next
            nextNode.next = currNode
            currNode = nextNode
            nextNode = reserved
        
        # reorder (First Half <=  Second half)
        tail = currNode
        while tail:
            reservedHead = head.next
            reservedTail = tail.next
            head.next = tail
            tail.next = reservedHead
            head = reservedHead
            tail = reservedTail
        # Fine to leave tail even if remaining as it's linked