# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        curr = head
        size = 0
        while curr and size < k:
            curr = curr.next
            size += 1
        
        if size == k:
            prev = self.reverseKGroup(curr, k) # Get reversed next blocks
            curr = head
            while curr and size:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
                size -= 1
            head = prev
        return head