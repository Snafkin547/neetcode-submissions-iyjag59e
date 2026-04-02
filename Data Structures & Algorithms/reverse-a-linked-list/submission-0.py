# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Reverse pointers
        # Keep next and prev
        # Redirect curr to prev
        # update curr to next
        # Do this till no next and return curr at the end
        
        prev = None
        curr = head
        while curr:
            Next = curr.next
            curr.next = prev
            prev = curr
            curr = Next
        return prev

        