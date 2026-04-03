# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast = head
        slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        # Reverse slow
        reverse = slow.next
        slow.next = None # So we know the end
        prev = None
        while reverse:
            temp = reverse.next
            reverse.next = prev
            prev = reverse
            reverse = temp

        # Weave
        while prev:
            f_temp = head.next
            head.next = prev # Weave prev after head
            head = f_temp # Move forward head forward

            p_temp = prev.next
            prev.next = head # Weave next head after prev
            prev =  p_temp # Move backward head forward

        