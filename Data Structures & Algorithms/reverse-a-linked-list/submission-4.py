# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        
        node = head
        if head.next:
            node = self.reverseList(head.next) # returns new head
            head.next.next = head # reverse curr one
        head.next = None # Necessary only for the first caller layer, the inner layer ovevrwrite by the line above 
        return node