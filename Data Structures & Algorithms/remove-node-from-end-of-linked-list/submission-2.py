# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = node = ListNode()
        node.next = head
        for i in range(n):
            head = head.next
        while head:
            node = node.next
            head = head.next
        node.next = node.next.next
        return dummy.next
        

        